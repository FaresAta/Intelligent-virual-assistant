import os
import PyPDF2
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import HumanMessage
from pinecone import Pinecone, ServerlessSpec
from math import ceil
import re
import pandas as pd

from prerequisites import (
    DS_prerequisites,
    AI_prerequisites,
    CS_prerequisites,
    CIS_prerequisites,
    BIT_prerequisites,
    Cyber_prerequisites,
    course_descriptions 
)


# API Keys
OPENAI_API_KEY = ""
PINECONE_API_KEY = ""
PINECONE_ENVIRONMENT = "us-east-1"
INDEX_NAME = "example4"
NAMESPACE = "consolidated_namespace"  # Replace with your desired namespace


# Initialize LangChain Components
embed_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY)
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

# Initialize Pinecone Client
pinecone_client = Pinecone(api_key=PINECONE_API_KEY)

# Check if the index exists, otherwise create it
if INDEX_NAME not in [index["name"] for index in pinecone_client.list_indexes()]:
    pinecone_client.create_index(
        name=INDEX_NAME,
        dimension=1536,  # Embedding dimension for "text-embedding-ada-002"
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=PINECONE_ENVIRONMENT
        )
    )

# Connect to the index
index = pinecone_client.Index(INDEX_NAME)


def extract_text_from_folder(folder_path):
    """
    Extract text from all PDFs and Excel files in the specified folder.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        dict: A dictionary where keys are file names and values are the extracted texts.
    """
    extracted_texts = {}
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if file_name.endswith(".pdf"):
            try:
                text = ""
                with open(file_path, "rb") as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                extracted_texts[file_name] = text
                print(f"Extracted text from PDF: {file_name}")
            except Exception as e:
                print(f"Failed to process PDF {file_name}: {e}")
        
        elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            try:
                df = pd.read_excel(file_path)
                texts = []
                for index, row in df.iterrows():
                    row_text = ' | '.join([f"{col}: {row[col]}" for col in df.columns])
                    texts.append(row_text)
                extracted_texts[file_name] = '\n\n'.join(texts)
                print(f"Extracted text from Excel: {file_name}")
            except Exception as e:
                print(f"Failed to process Excel file {file_name}: {e}")
    
    return extracted_texts



def make_chunks(text, chunk_size=300, overlap=50):
    """Split text into manageable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return text_splitter.split_text(text)


def embed_text(chunks):
    """Embed text chunks using OpenAI."""
    return embed_model.embed_documents(chunks)


def batch_upsert(index, vectors, batch_size=100, namespace=NAMESPACE):
    """Batch upsert vectors into Pinecone index."""
    total_vectors = len(vectors)
    num_batches = ceil(total_vectors / batch_size)
    for i in range(num_batches):
        batch = vectors[i * batch_size: (i + 1) * batch_size]
        index.upsert(vectors=batch, namespace=namespace)
        print(f"Upserted batch {i + 1}/{num_batches} into namespace '{namespace}'")




def prepare_vectorstore(chunks, embeddings, namespace=NAMESPACE):
    """Set up Pinecone vectorstore with embedded chunks."""
    vectors = [{"id": f"chunk-{i+1}", "values": embedding, "metadata": {"text": chunk}}
               for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))]

    print(f"Prepared {len(vectors)} vectors for upsert.")
    batch_upsert(index, vectors, namespace=namespace)

    # Verify vector count in Pinecone
    try:
        stats = index.describe_index_stats()
        print(f"After upsert, Pinecone stats: {stats}")
    except Exception as e:
        print(f"Failed to fetch Pinecone stats: {e}")

    return PineconeVectorStore(index=index, embedding=embed_model, namespace=namespace)


import re

def extract_course_name(query, all_courses, course_aliases):
    """
    Extracts a valid course name from the query.
    Supports exact matches, abbreviation-based matches, and prevents incorrect partial matches.
    """
    query = query.lower().strip()

    # ✅ First, check if an alias (e.g., "ML" → "Machine Learning") exists as a full word in the query
    for alias, full_name in course_aliases.items():
        if re.search(rf"\b{re.escape(alias.lower())}\b", query):  # Ensure full-word match
            print(f"🔄 Matched alias: {alias} → {full_name}")
            query = re.sub(rf"\b{re.escape(alias.lower())}\b", full_name.lower(), query)

    # ✅ Try exact match first
    for course, details in all_courses.items():
        if course.lower() == query or details.get("arabic_name", "").lower() == query:
            return course  # Exact match found

    # ✅ Try full-word match (not just substring matching)
    for course, details in all_courses.items():
        if re.search(rf"\b{re.escape(course.lower())}\b", query) or re.search(rf"\b{re.escape(details.get('arabic_name', '').lower())}\b", query):
            return course  # Partial but valid full-word match found

    return None  # No valid match found



def detect_language(query):
    """Use OpenAI to determine if the query is in Arabic or English."""
    detection_prompt = f"Detect if this query is Arabic or English: {query}\nRespond with only 'Arabic' or 'English'."
    response = chat.invoke([HumanMessage(content=detection_prompt)])
    return response.content.strip()


def answer_query(query, vectorstore, namespace=NAMESPACE):
    """Answer a query using prerequisites, course descriptions, and Pinecone for general knowledge."""

    print(f"Running query in namespace: {namespace}")

    # ✅ Detect query language (Arabic if any Arabic Unicode characters are present)
    query_language = detect_language(query)
    print(f"Detected query language: {query_language}")
    
    # Normalize detected language for comparison
    if query_language:
        query_language = query_language.lower()

    # ✅ Normalize query for better matching
    normalized_query = query.lower().strip()

    greetings = {
        "english": ["hi", "hello", "hey", "good morning", "good evening", "good afternoon", "how are you", "what's up"],
        "arabic": ["مرحبا", "أهلا", "السلام عليكم", "مساء الخير", "صباح الخير", "كيف حالك", "شو الأخبار"]
    }

    farewell = {
        "english": ["bye", "goodbye", "see you", "take care", "later"],
        "arabic": ["مع السلامة", "وداعا", "إلى اللقاء", "اهتم بنفسك"]
    }

    thanks = {
        "english": ["thank you", "thanks", "appreciate it", "thank u"],
        "arabic": ["شكرا", "أشكرك", "ممنون"]
    }

    # ✅ Check for Greetings
    if any(re.search(rf"\b{re.escape(word)}\b", normalized_query) for word in greetings["english"] + greetings["arabic"]):
        return "Hello! How can I assist you today? 😊" if query_language == "english" else "مرحبا! كيف بقدر اساعدك اليوم؟ 😊"

    # ✅ Check for Farewells
    if any(re.search(rf"\b{re.escape(word)}\b", normalized_query) for word in farewell["english"] + farewell["arabic"]):
        return "Goodbye! Have a great day! 👋" if query_language == "english" else "وداعا! أتمنى لك يوما رائعا! 👋"

# ✅ Check for Thanks
    if any(re.search(rf"\b{re.escape(word)}\b", normalized_query) for word in thanks["english"] + thanks["arabic"]):
        return "You're welcome! Let me know if you need anything else. 😊" if query_language == "english" else "على الرحب والسعة! أخبرني إذا كنت بحاجة إلى أي شيء آخر. 😊"
    

    # ✅ Merge dictionaries for lookup
    all_prerequisites = {**DS_prerequisites, **AI_prerequisites, **CS_prerequisites, 
                          **CIS_prerequisites, **BIT_prerequisites, **Cyber_prerequisites}
    all_courses = course_descriptions  

    # ✅ Keywords for prerequisite-related queries
    prerequisite_keywords = [
        "prerequisite", "requirement", "needed", "before", "precondition",
        "مطلوب", "متطلبات", "قبل", "الشرط الأساسي", "ما الذي يجب أن أتعلمه قبل"
    ]

    # ✅ Course synonyms & abbreviations for better matching
    course_aliases = {
        "ML": "Machine Learning", "تعلم الآلة": "Machine Learning",
        "DL": "Deep Learning", "التعلم العميق": "Deep Learning",
        "CS": "Computer Science", "علم الحاسوب": "Computer Science",
        "AI": "Artificial Intelligence", "الذكاء الاصطناعي": "Artificial Intelligence",
        "DS": "Data Science", "علوم البيانات": "Data Science",
        "CIS": "Computer Information Systems", "نظم المعلومات الحاسوبية": "Computer Information Systems",
        "BIT": "Business Information Technology", "تكنولوجيا المعلومات الإدارية": "Business Information Technology",
        "Cyber": "Cyber Security", "الأمن السيبراني": "Cyber Security",
        "DB": "Database", "قواعد البيانات": "Database",
        "Algo": "Algorithms", "الخوارزميات": "Algorithms",
        "OOP": "Object-Oriented Programming", "البرمجة الكائنية": "Object-Oriented Programming",
        "PL": "Programming Languages", "لغات البرمجة": "Programming Languages"
    }


    # ✅ Replace aliases in query (e.g., "ML" → "Machine Learning")
    for alias, full_name in course_aliases.items():
        if re.search(rf"\b{re.escape(alias.lower())}\b", normalized_query):
            print(f"🔄 Matched alias: {alias} → {full_name}")
            normalized_query = re.sub(rf"\b{re.escape(alias.lower())}\b", full_name.lower(), normalized_query)

    # ✅ Extract course name from the query
    matched_course = None
    for course, details in all_courses.items():
        normalized_course_en = course.lower().strip()
        normalized_course_ar = details.get("arabic_name", "").lower().strip()

        if re.search(rf"\b{re.escape(normalized_course_en)}\b", normalized_query) or re.search(rf"\b{re.escape(normalized_course_ar)}\b", normalized_query):
            matched_course = course
            break

    # ✅ If the query is about a course prerequisite
    if matched_course and any(keyword in normalized_query for keyword in prerequisite_keywords):
        prereq_courses = all_prerequisites.get(matched_course, [])
        print(f"📌 Matched Course: {matched_course}")

        if prereq_courses:
            prereq_list = ", ".join(prereq_courses)
            return f"The prerequisites for {matched_course} are: {prereq_list}." if query_language == "English" else f"المتطلبات السابقة لمادة {matched_course} هي: {prereq_list}."
        else:
            return f"{matched_course} has no prerequisites." if query_language == "english" else f"مادة {matched_course} ليس لها متطلبات سابقة."

    # ✅ If the query is asking about a course description
    if matched_course:
        course_info = all_courses.get(matched_course, {})
        if course_info:
            return course_info.get("description_en" if query_language == "english" else "description_ar")

    # ✅ If no match is found in the course database, FALL BACK to Pinecone!
    print("⚠️ No course matched in prerequisites or descriptions! Searching Pinecone database...")

    results = vectorstore.similarity_search_with_score(query, k=9, namespace=namespace)
    relevant_results = [x[0].page_content for x in results if x[1] >= 0.75]  # Only use results with high confidence
    source_knowledge = "\n".join(relevant_results).strip()

    # ✅ Handle cases where no relevant data is found
    if not relevant_results:
        return "لا توجد معلومات ذات صلة." if query_language == "arabic" else "No relevant information found."

    # ✅ Create the augmented prompt
    augmented_prompt = f"""
    You are a helpful assistant so focus to help the students, Using the contexts below, answer the query strictly in {query_language}. 
    Only provide an answer if it can be derived from the contexts.
    If the information is not available in the contexts, respond with "No relevant information found." in {query_language}.

    Contexts:
    {source_knowledge}

    Query: {query}
    """

    print(f"Augmented Prompt:\n{augmented_prompt}")

    # ✅ Send the prompt to the chat model
    prompt = HumanMessage(content=augmented_prompt)
    response = chat.invoke([prompt])

    # ✅ Ensure the response is not too long
    response_text = response.content.strip()
    max_length = 1000
    if len(response_text) > max_length:
        response_text = response_text[:max_length] + "..."

    return response_text




def clear_pinecone_namespaces(index, namespaces):
    """Clear specified namespaces in the Pinecone index."""
    for ns in namespaces:
        try:
            print(f"Clearing namespace: {ns}")
            index.delete(delete_all=True, namespace=ns)
        except Exception as e:
            print(f"Failed to clear namespace '{ns}': {e}")


def initialize_backend(folder_path, namespace=NAMESPACE):

    #existing_namespaces = ["consolidated_namespace", "default"]
    #clear_pinecone_namespaces(index, existing_namespaces)

    print("Starting backend initialization...")

    try:
        print("Extracting text from PDFs...")
        extracted_texts = extract_text_from_folder(folder_path)

        print("Splitting text into chunks...")
        chunks = [chunk for text in extracted_texts.values() for chunk in make_chunks(text)]
        print(f"Total Chunks Created: {len(chunks)}")

        print("Embedding text chunks...")
        embeddings = embed_text(chunks)
        print(f"Total Embeddings Created: {len(embeddings)}")

        print("Setting up Pinecone vectorstore...")
        vectorstore = prepare_vectorstore(chunks, embeddings, namespace=namespace)

        print("\nPinecone Index Summary:")
        stats = index.describe_index_stats()
        print(stats)

        print("Backend initialization complete.")
        return vectorstore

    except Exception as e:
        print(f"Error during backend initialization: {e}")
        raise



# Example Usage (for Testing)
if __name__ == "__main__":
    folder_path = r"C:\Users\Asus\OneDrive - AmberX\JU\graduation project 3\real_data"
    vectorstore = initialize_backend(folder_path, namespace="consolidated_namespace")

    #Simulate query answering
 # Simulate query answering in a loop
# while True:
#     user_query = input("Enter your query (or type 'exit' to quit): ")
#     if user_query.lower() in ["exit", "quit"]:
#         print("Exiting. Goodbye!")
#         break
#     response = answer_query(user_query, vectorstore, namespace="consolidated_namespace")
#     print(f"AI: {response}")


    #response = answer_query("What is wavesJU ?", vectorstore, namespace="consolidated_namespace")
    #print(response)
# test_queries = ["hi", "Hello", "مرحبا", "أهلا"]
# for q in test_queries:
#     print(f"Input: {q}")
#     # Simulate detection (if detect_language is not working as expected, temporarily hard-code it)
#     lang = "english" if q.lower() in greetings["english"] else "arabic"
#     print("Normalized query:", q.lower().strip())
#     print("Response:", answer_query(q, vectorstore))  # Or call your function directly


