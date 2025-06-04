import flet as ft
import threading
import sqlite3
import re
import webbrowser
from threading import Lock
from backend import initialize_backend, answer_query
from table_generator2 import generate_all_schedules
import json
import os

chat_messages = None  # Initialize chat_messages as None

chat_history = []
current_chat = None
current_dialog = None



def hover_shadow(e):
    """
    Adds a subtle shadow when hovering over the Container.
    e.data == "true"  => pointer entered
    e.data == "false" => pointer left
    """
    c = e.control  # The control that received the hover event (our Container)
    if e.data == "true":
        # Apply a shadow
        c.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=4,
            color="#424242",  # Changed from ft.colors.BLACK26
            offset=ft.Offset(0, 2)    # a slight vertical offset
        )
    else:
        # Remove the shadow
        c.shadow = None
    c.update()  # Force the Container to update its UI




def close_dialog(page):
    global current_dialog
    if current_dialog:
        current_dialog.open = False
        try:
            page.overlay.remove(current_dialog)
        except ValueError:
            # Dialog may already be removed
            pass
        current_dialog = None
    page.update()




def handle_chat_click(e, chat, page, user_id):
    """Handles when a user selects a chat from history."""
    close_dialog(page)  # ✅ Close chat selection dialog immediately

    # ✅ Load the selected chat directly
    load_chat(chat, page, user_id)  # ✅ Pass user_id to load_chat





def load_chat_history(user_id):
    """Load chat history for a specific user from a file."""
    filename = f"chat_history_{user_id}.json"  # Unique file per user
    if not os.path.exists(filename):
        return []  # Return empty list if no history exists
    
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"❌ Error decoding chat history for user {user_id}. Returning empty history.")
        return []
    
def save_chat_history(user_id, chat_history):
    """Save chat history for a specific user to a file."""
    filename = f"chat_history_{user_id}.json"  # Save in user-specific file
    with open(filename, "w") as file:
        json.dump(chat_history, file, indent=4)


    
def rename_chat(chat, page, user_id):
    global chat_history, current_chat

    def save_new_name(e):
        new_name = rename_field.value.strip()
        if new_name:
            # Update the name in chat_history
            for c in chat_history:
                if c is chat:
                    c["name"] = new_name
                    break
            # If we're renaming the currently active chat:
            if current_chat is chat:
                current_chat["name"] = new_name

            # Save updated history
            save_chat_history(user_id, chat_history)  # ✅ Now correctly passes user_id


            # Close the rename dialog
            rename_dialog.open = False
            page.update()

            # (Optional) You can reopen chat history if you wish:
            display_chat_history(None, page, user_id)

    # Create the text field & save button
    rename_field = ft.TextField(
        hint_text="Enter new name", 
        expand=True, 
        on_submit=save_new_name
    )
    rename_button = ft.ElevatedButton("Save", on_click=save_new_name)

    # Create the rename dialog
    rename_dialog = ft.AlertDialog(
        title=ft.Text("Rename Chat"),
        content=ft.Container(
            content=ft.Column([rename_field, rename_button], spacing=10),
            width=400,
            height=250,
        ),
        actions=[],  # We'll add the close button next
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Local function to close the rename dialog
    def close_rename_dialog(e):
        rename_dialog.open = False
        page.update()

    # Add a "Close" button
    rename_dialog.actions = [
        ft.TextButton("Close", on_click=close_rename_dialog)
    ]

    # Show the dialog
    page.overlay.append(rename_dialog)
    rename_dialog.open = True
    page.update()




def display_chat_history(e, page, user_id):
    global chat_history
    
    chat_list = ft.ListView(expand=True, spacing=5, auto_scroll=False)

    def delete_chat(e, chat, user_id):
        """Delete the selected chat from chat history."""
        global chat_history
        chat_history.remove(chat)
        save_chat_history(user_id, chat_history)  # ✅ Save updated chat history
        display_chat_history(e, page, user_id)  # ✅ Refresh UI

    if not chat_history:
        chat_list.controls.append(ft.Text("⚠️ No previous chats found!", color="red"))
    else:
        for chat in chat_history:
            chat_list.controls.append(
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(chat['name'], color="black"),
                            padding=10,
                            bgcolor="white",
                            border_radius=ft.border_radius.all(15),
                            expand=True,  # Ensures text does not push buttons outside
                            on_click=lambda e, chat=chat: handle_chat_click(e, chat, page, user_id),  # ✅ Pass `page`
                            on_hover=hover_shadow,
                        ),
                        ft.IconButton(
                            icon="edit",
                            on_click=lambda e, chat=chat: rename_chat(chat, page, user_id)
                        ),
                        ft.IconButton(
                            icon="delete",
                            icon_color="red",
                            tooltip="Delete Chat",
                            on_click=lambda e, chat=chat: delete_chat(e, chat, user_id)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Ensures even spacing
                )
            )

    # ✅ Add "New Chat" Button Inside Dialog
    new_chat_button = ft.ElevatedButton(
        text="New Chat",
        icon="add",
        bgcolor="#2c3744",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),  
        on_click=lambda e: create_new_chat(page, user_id)
    )

    # ✅ Add Button Below Chat List
    dialog_content = ft.Column(
        controls=[
            chat_list, 
            ft.Container(new_chat_button, alignment=ft.alignment.center)
        ],
        spacing=10
    )

    # ✅ Create Dialog with New Chat Button Inside
    dialog = ft.AlertDialog(
        title=ft.Text("Chat History"),
        content=ft.Container(content=dialog_content, width=400, height=300),
        actions=[ft.TextButton("Close", on_click=lambda e: close_this_dialog(e))],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def close_this_dialog(e):
        """Properly close the chat history dialog."""
        dialog.open = False
        page.update()

    page.overlay.append(dialog)
    dialog.open = True
    page.update()





def load_chat(chat, page, user_id):
    """Load a specific chat into the chat UI."""
    global chat_messages, current_chat, suggestions_container

    # ✅ Set the selected chat as the current chat
    current_chat = chat  

    # ✅ Clear chat UI before loading new messages
    chat_messages.controls.clear()
    
    # ✅ Remove suggestions when loading a chat
    suggestions_container.controls.clear()

    chat_messages.update()  # ✅ Force UI update before adding messages
    suggestions_container.update()

    bot_bgcolor = "#002137"   # Bot message background color
    user_bgcolor = "#003356"  # User message background color

    # ✅ Reload messages from the selected chat
    for message in chat["messages"]:
        if message["sender"] == "Bot":
            chat_messages.controls.append(
                ft.Row(
                    controls=[
                        ft.Image(
                            src=bot_icon,
                            width=35,
                            height=35,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Container(
                            content=ft.Text(message["message"], color="white", size=14),
                            padding=10,
                            bgcolor="#002137",  
                            border_radius=ft.border_radius.all(15),
                            width=250
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            )
        else:
            chat_messages.controls.append(
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(message["message"], color="white", size=14),
                            padding=ft.padding.symmetric(horizontal=12, vertical=8),
                            bgcolor="#003356",  
                            border_radius=ft.border_radius.all(15), 
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            )

    # ✅ Force a full UI update after reloading messages
    chat_messages.update()
    suggestions_container.update()  # ✅ Ensure UI removes old suggestions
    page.update()







def create_new_chat(page, user_id):
    global current_chat, chat_messages, chat_history  

    # ✅ Avoid creating a new chat if there's already an active chat
    if current_chat and current_chat["messages"]:
        save_chat_history(user_id, chat_history)  # ✅ Save only if there are messages

    # ✅ Clear the UI for the new chat
    chat_messages.controls.clear()
    page.update()

    # ✅ Only create a new chat when necessary
    current_chat = {"name": "New Chat", "messages": []}
    chat_history.append(current_chat)
    save_chat_history(user_id, chat_history)  # ✅ Save after creating a new chat



# ✅ Initialize Backend
folder_path = r"C:\Users\Asus\OneDrive - AmberX\JU\graduation project 3\real_data"
try:
    print("Initializing backend, please wait...")
    vectorstore = initialize_backend(folder_path)
    print("Backend initialized successfully.")
except Exception as e:
    print(f"Failed to initialize backend: {e}")
    vectorstore = None

# ✅ Function to open Google Maps
def open_google_maps(destination):
    if not destination.strip():
        return "Please specify a destination."
    google_maps_url = f"https://www.google.com/maps/dir/?api=1&destination={destination.replace(' ', '+')}"
    webbrowser.open(google_maps_url)
    return f"Opening Google Maps for directions to: {destination}"

# ✅ List of phrases for Google Maps queries
maps_phrases = ["how to go to", "directions to", "navigate to", "take me to", "how to get to", "navigate me to", "how do i go to", "how do i get to", "كيف اروح ل", "كيف اروح على"]

# ✅ Path to University of Jordan logo
uj_logo_path = r"C:\Users\Asus\OneDrive - AmberX\JU\graduation project 3\Design pages\logo.jpg"
bot_icon = r"C:\Users\Asus\OneDrive - AmberX\JU\graduation project 3\Design pages\chat logo.png"



# ✅ Function to simulate typing effect
def type_writer_effect(full_text: str, text_widget: ft.Text, page: ft.Page, delay=0.1):
    """Simulate typing effect into an existing Text widget."""
    def update_text(i):
        # Only update this specific text widget
        text_widget.value = full_text[:i]
        page.update()

    # Schedule each character update
    for i in range(1, len(full_text) + 1):
        threading.Timer(i * delay, update_text, [i]).start()

    
# **MAIN FUNCTION**
def chatbot_ui(page: ft.Page, user_id, home_page):
    """Load the chatbot UI after successful login and manage user chats separately."""
    page.clean()  # Clear the page before adding new content
    global chat_messages, current_chat, chat_history, suggestions_container  # Declare chat_messages and current_chat as global to modify them within the function
    page.title = "JU Virtual Assistant"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f5fbf9"

    # ✅ FIXED WINDOW SETTINGS
    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False
    page.padding = 0

    # ✅ Load chat history BEFORE setting up chat UI
    chat_history = load_chat_history(user_id)  

    # ✅ Ensure chat_history is always a valid list
    if not isinstance(chat_history, list):
        chat_history = []

    # ✅ Always create a new chat session when the program starts
    current_chat = {"name": "New Chat", "messages": []}
    chat_history.append(current_chat)
    save_chat_history(user_id, chat_history)

    # ✅ Initialize chat_messages
    chat_messages = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, controls=[], spacing=10)

    # ✅ Restore messages from last chat
    for message in current_chat["messages"]:
        if message["sender"] == "Bot":
            chat_messages.controls.append(
                ft.Row(
                    controls=[
                        ft.Image(src=bot_icon, width=35, height=35, fit=ft.ImageFit.CONTAIN),
                        ft.Container(
                            content=ft.Text(message["message"], color="white", size=14),
                            padding=10,
                            bgcolor="#002137",
                            border_radius=ft.border_radius.all(15),
                            width=250
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            )
        else:  # ✅ User messages
            chat_messages.controls.append(
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(message["message"], color="white", size=14),
                            padding=ft.padding.symmetric(horizontal=12, vertical=8),
                            bgcolor="#003356",
                            border_radius=ft.border_radius.all(15),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            )


    #-chat_messages.update()  # ✅ Ensure UI updates with restored messages



    def send_message(e):
        """Handles message sending and saves to Firebase under the correct user ID."""
        message = user_input.value.strip()
        if message:
            chat_messages.controls.append(ft.Text(message, color="black"))
            user_input.value = ""
            page.update()
            if current_chat is None:
                current_chat = {"name": "New Chat", "messages": []}
                chat_history.append(current_chat)  # ✅ Ensure it's stored

            current_chat["messages"].append({"sender": "User", "message": message})  # ✅ Store message in the correct chat session
            save_chat_history(user_id, chat_history)  # ✅ Save updated history

            
    def chat_page():
        # ✅ Load chat history from file
        chat_history = load_chat_history()


    def handle_logout(e, page):
        """Logs out the user and redirects to the home page."""
        page.clean()  # Clear everything
        home_page()  # ✅ Call home_page() function directly
        page.update()


    # ✅ Chat History Button
# ✅ Logout Button (Top Left)
    logout_button = ft.IconButton(
        icon="logout",
        icon_color="red",
        tooltip="Logout",
        on_click=lambda e: handle_logout(e, page)  # ✅ Calls handle_logout
    )

    # ✅ Chat History Button (Top Right)
    chat_history_button = ft.IconButton(
        icon="history",
        icon_color="#2c3744",
        tooltip="Chat History",
        on_click=lambda e: (close_dialog(page), display_chat_history(e, page, user_id))
    )

    # ✅ Updated Header Bar
    header = ft.Container(
        content=ft.Row(
            controls=[
                logout_button,  # Logout button on the left
                ft.Container(expand=True),  # Pushes title to center
                ft.Text("UniGuide", color="#2c3744", size=18, weight=ft.FontWeight.BOLD),
                ft.Container(expand=True),  # Pushes history button to right
                chat_history_button  # Chat History button on the right
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Space buttons correctly
        ),
        padding=ft.padding.symmetric(horizontal=15, vertical=10),
        bgcolor="#f5fbf9",
        border=ft.border.only(bottom=ft.border.BorderSide(1, "white"))  # White border at bottom
    )


    # ✅ Chat messages container
    chat_messages = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, controls=[], spacing=10)


    # ✅ Add suggestion buttons when the chatbot opens
    suggestions_container = ft.Column(spacing=10, alignment=ft.MainAxisAlignment.CENTER)

    def show_suggestions():
        suggestions = [
            "How are you ?",
            "شو هو نظام التسجيل الذاتي بالجامعة الأردنية ؟",
            "كيف بقدر اقدم للحصول على منح دراسية ؟",
            "What time are Dr.Iman's office hours ?",
            "شو لازم انزل قبل التعلم العميق ؟",
        ]

        # Function to handle button click and remove buttons after selection
        def update_user_input(e):
            user_input.value = e.control.text  # Set text field value
            suggestions_container.controls.clear()  # Remove buttons after selection
            page.update()
            process_query(None)  # Process query automatically

        # Create buttons inside a centered column
        suggestion_buttons = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text=suggestion,
                    bgcolor="#002137",
                    color="white",
                    width=300,  # Set uniform width
                    height=45,
                    on_click=update_user_input,
                ) for suggestion in suggestions
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Center vertically
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center horizontally
            spacing=10,  # Add spacing between buttons
        )

        # Clear previous suggestions and add new ones inside chat area
        suggestions_container.controls.clear()
        suggestions_container.controls.append(suggestion_buttons)
        page.update()

    # Call show_suggestions here to ensure it's called when the page loads
    show_suggestions()

    # Create a lock instance to prevent duplicate queries
    query_lock = Lock()



    def run_query(query, chat_messages, page):
        """Process user query while keeping chat memory."""

        try:
            # ✅ Send only the query (Remove appending past messages)
            response = answer_query(query, vectorstore)  

            # ✅ Log response to verify backend is retrieving data correctly
            print(f"🔍 Backend Response: {response}")

            if not response:
                response = "⚠️ No relevant answer found."

            # ✅ Append bot's response to UI
            bot_text = ft.Text("", color="white")
            bot_row = ft.Row(
                controls=[
                    ft.Image(
                        src=bot_icon,
                        width=35,
                        height=35,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Container(
                        content=bot_text,
                        padding=10,
                        bgcolor="#002137",
                        border_radius=ft.border_radius.all(15),
                        width=250
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            )
            chat_messages.controls.append(bot_row)
            page.update()

            # ✅ Typing effect for bot response
            type_writer_effect(response, bot_text, page, delay=0.03)

            # ✅ Save response to chat history
            with query_lock:
                current_chat["messages"].append({"sender": "Bot", "message": response})
                save_chat_history(user_id, chat_history)  # ✅ Now correctly passes user_id


        except Exception as ex:
            chat_messages.controls.append(ft.Text(f"❌ Error: {ex}", color="red"))
        finally:
            page.update()



    def process_query(e):
        """Handles user input and processes query accordingly."""
        global current_chat  

        query = user_input.value.strip().lower()
        if not query:
            chat_messages.controls.append(ft.Text("⚠️ Please enter a query!", color="orange"))
            page.update()
            return

        suggestions_container.controls.clear()  # Remove suggestions on manual input
        page.update()

        if query_lock.locked():
            return  # Prevent duplicate execution

        with query_lock:
            # ✅ Ensure chat is restored instead of creating a new one each time
            if current_chat is None:
                if chat_history:
                    current_chat = chat_history[-1]  # Load last chat instead of resetting
                else:
                    current_chat = {"name": "New Chat", "messages": []}
                    chat_history.append(current_chat)

            # ✅ Check for Google Maps request
            if any(phrase in query for phrase in maps_phrases):
                destination = query.split("to")[-1].strip()  # Extract destination
                response = open_google_maps(destination)

                # ✅ Display user query
                chat_messages.controls.append(
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(query, color="#f5fbf9"),
                                padding=10,
                                bgcolor="#003356",
                                border_radius=ft.border_radius.all(15)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    )
                )

                # ✅ Display Google Maps response
                chat_messages.controls.append(ft.Text(response, color="blue"))

                # ✅ Save Google Maps response to history
                current_chat["messages"].append({"sender": "User", "message": query})
                current_chat["messages"].append({"sender": "Bot", "message": response})
                save_chat_history(user_id, chat_history)  # ✅ Now correctly saves history

                page.update()
                return  # ✅ Exit early, no need to process with backend

            # ✅ If first user message, rename chat
            if current_chat and not current_chat["messages"]:
                truncated_name = query[:30] + "..." if len(query) > 30 else query
                current_chat["name"] = truncated_name
                save_chat_history(user_id, chat_history)  # ✅ Now correctly passes user_id

            # ✅ Save user message
            current_chat["messages"].append({"sender": "User", "message": query})
            save_chat_history(user_id, chat_history)  # ✅ Now correctly passes user_id

            # ✅ Display user message in UI
            chat_messages.controls.append(
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(query, color="#f5fbf9"),
                            padding=10,
                            bgcolor="#003356",
                            border_radius=ft.border_radius.all(15)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )
            )

            user_input.value = ""
            page.update()

            # ✅ Process query with chat memory
            threading.Thread(target=run_query, args=(query, chat_messages, page), daemon=True).start()









    user_input = ft.TextField(
        hint_text="Type a message",
        expand=True,
        border_radius=25,
        border_color="white",
        content_padding=ft.padding.all(12),
        text_size=16,
        text_style=ft.TextStyle(color="#2c3744"),
        on_submit=process_query
    )


    def show_schedule_page(page, schedules):
        """Display the generated schedules in a structured table format with correct sorting & full course names."""

        schedule_container = ft.Column(scroll="adaptive", expand=True)  # ✅ No bgcolor here

        def return_to_table_generator(e):
            """Return to the Table Generator page."""
            page.views.pop()  # ✅ Remove the current view (go back)
            page.go("/table_generator")  # ✅ Navigate back

        def extract_start_time(time_str):
            """Extracts start time (HH:MM) and ensures correct sorting based on Arabic day priority."""
            match = re.search(r"(\d{2}):(\d{2})-(\d{2}):(\d{2}) \(([^)]+)\)", time_str)
            if match:
                start_hour, start_minute, _, _, days = match.groups()
                # ✅ Strict priority for Arabic days
                day_priority = 0 if any(d in days for d in ["ح", "ث", "خ"]) else 1 if any(d in days for d in ["ن", "ر"]) else 2
                return (day_priority, int(start_hour), int(start_minute))  # Sort by priority, then time
            return (99, 99, 99)  # Fallback for invalid parsing

        # ✅ Handle case where no schedules are found
        if not schedules:
            schedule_container.controls.append(
                ft.Text("⚠️ No valid schedules found!", color="red", size=16, text_align=ft.TextAlign.CENTER)
            )
        else:
            for idx, schedule in enumerate(schedules, start=1):
                sorted_schedule = sorted(schedule, key=lambda c: extract_start_time(c[3]))

                # ✅ Table Header
                schedule_container.controls.append(
                    ft.Container(
                        content=ft.Text(
                            f"Table {idx} - Recommended Schedule",
                            weight=ft.FontWeight.BOLD,
                            size=18,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        padding=ft.padding.symmetric(vertical=10),
                        alignment=ft.alignment.center,
                    )
                )

                # ✅ Data Table
                table = ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Course", weight=ft.FontWeight.BOLD, size=14)),
                        ft.DataColumn(ft.Text("Section", weight=ft.FontWeight.BOLD, size=14), numeric=True),
                        ft.DataColumn(ft.Text("Time", weight=ft.FontWeight.BOLD, size=14, text_align=ft.TextAlign.CENTER)),
                        ft.DataColumn(ft.Text("Room", weight=ft.FontWeight.BOLD, size=14, text_align=ft.TextAlign.CENTER)),
                        ft.DataColumn(ft.Text("Status", weight=ft.FontWeight.BOLD, size=14, text_align=ft.TextAlign.CENTER)),
                    ],
                    rows=[],
                    column_spacing=15,
                    data_row_color={"hovered": "#F5F5F5"},
                    divider_thickness=1,
                )

                for course_code, course_name, section, time, group_type, room, status in sorted_schedule:
                    status_msg = "Available" if status != "مغلق" else "Full"
                    status_color = "green" if status != "مغلق" else "red"

                    table.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Container(ft.Text(course_name, size=12, text_align=ft.TextAlign.CENTER), expand=True, alignment=ft.alignment.center)),
                                ft.DataCell(ft.Container(ft.Text(f"{section}", size=12, text_align=ft.TextAlign.CENTER), alignment=ft.alignment.center)),
                                ft.DataCell(ft.Text(f"{time} ({group_type})", size=12, text_align=ft.TextAlign.CENTER)),
                                ft.DataCell(ft.Text(f"{room}", size=12, text_align=ft.TextAlign.CENTER)),
                                ft.DataCell(ft.Text(status_msg, size=12, color=status_color, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)),
                            ]
                        )
                    )

                schedule_container.controls.append(table)

        # ✅ Full-page schedule view with proper background color
        schedule_page = ft.View(
            route="/schedule_page",
            controls=[
                # ✅ Header with Back Button
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton("arrow_back", on_click=return_to_table_generator),
                            ft.Text("Generated Schedule", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color="#2c3744"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    padding=10,
                    bgcolor="#f5fbf9"  # ✅ Background applied to header
                ),
                # ✅ Schedule Container Wrapped in Container for bgcolor
                ft.Container(
                    content=schedule_container,
                    expand=True,
                    bgcolor="#f5fbf9"  # ✅ Background applied to schedule container
                ),
            ],
            bgcolor="#f5fbf9"  # ✅ Ensure the entire page has the correct background
        )

        page.views.append(schedule_page)
        page.update()
        page.go("/schedule_page")



    

    # ✅ Table Generator UI with Scrollable Courses and Search Bar
   # ✅ Table Generator UI with Scrollable Courses and Search Bar
    # ✅ Table Generator UI with Scrollable Courses and Search Bar
    def show_table_generator(page: ft.Page):
        """Display the course table generator with full-page course list and a search bar."""

        selected_courses = set()
        all_courses = []  # ✅ Store courses globally inside the function

        def update_selected_courses(e):
            """Handles course selection updates and ensures checkboxes persist."""
            course_code = e.control.data
            if e.control.value:
                selected_courses.add(course_code)
            else:
                selected_courses.discard(course_code)

            # ✅ Keep selection states even when filtering
            update_course_list(all_courses)


        def fetch_courses():
            """Fetch courses from SQLite database."""
            nonlocal all_courses  # ✅ Ensure we modify the global variable inside function
            try:
                conn = sqlite3.connect("courses.db")  # ✅ New connection per thread
                cursor = conn.cursor()
                cursor.execute("SELECT DISTINCT course_code, course_name FROM courses ORDER BY course_code")
                all_courses = cursor.fetchall()
                conn.close()
                update_course_list(all_courses)
            except Exception as e:
                print(f"❌ Error fetching courses: {e}")

        def update_course_list(filtered_courses):
            """Update UI with the fetched course list while maintaining selected checkboxes."""
            course_checkboxes.controls.clear()
            if not filtered_courses:
                course_checkboxes.controls.append(ft.Text("⚠️ No courses found!", color="red"))
            else:
                for code, name in filtered_courses:
                    checkbox = ft.Checkbox(
                        label=f"{code} - {name}",
                        data=code,
                        value=(code in selected_courses),  # ✅ Preserve selection state
                        on_change=update_selected_courses
                    )
                    course_checkboxes.controls.append(checkbox)
            page.update()


        def on_generate_clicked(e):
            """Generate course schedule tables and navigate to the schedule page."""
            if not selected_courses:
                error_text.value = "⚠️ Please select at least one course!"
                page.update()
                return

            error_text.value = ""  # Clear any previous error
            page.update()

            def fetch_schedules():
                try:
                    recommended_schedules = generate_all_schedules(list(selected_courses))
                    page.go("/schedule_page")  # ✅ Navigate to schedule page
                    show_schedule_page(page, recommended_schedules)
                except Exception as ex:
                    error_text.value = f"❌ Error: {str(ex)}"
                    page.update()

            # ✅ Run the schedule generation in a separate thread
            threading.Thread(target=fetch_schedules, daemon=True).start()

        def return_to_main(e):
            """Return to the chatbot main screen properly without UI freeze."""
            if len(page.views) > 1:
                page.views.pop()  # ✅ Properly remove only the last view
            page.go("/")  # ✅ Navigate back to main page

        def filter_courses(e):
            """Filters the course list based on search input."""
            query = search_box.value.lower().strip()
            filtered_courses = [course for course in all_courses if query in course[0].lower() or query in course[1].lower()]
            update_course_list(filtered_courses)

        # ✅ Define UI elements
        course_checkboxes = ft.ListView(expand=True, spacing=5, auto_scroll=False)
        search_box = ft.TextField(hint_text="🔍 Search courses...", on_change=filter_courses, expand=True)
        error_text = ft.Text("", color="red", size=14)

        full_page_ui = ft.View(
            route="/table_generator",
            controls=[
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.IconButton("arrow_back", on_click=return_to_main),
                            ft.Text("📚 Course Table Generator", size=20, weight=ft.FontWeight.BOLD, color="#2c3744"),
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    padding=10,
                    bgcolor="#f5fbf9"
                ),
                ft.Container(
                    search_box,
                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    bgcolor="#f5fbf9"
                ),
                ft.Container(
                    course_checkboxes,
                    expand=True,
                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    bgcolor="#f5fbf9"
                ),
                error_text,
                ft.ElevatedButton(
                    "Generate Tables",
                    on_click=on_generate_clicked,
                    bgcolor="#2c3744",
                    color="white"
                ),  
            ],
            bgcolor="#f5fbf9"
        )

        # ✅ Correctly handle view navigation
        if len(page.views) > 1:
            page.views.pop()  # ✅ Ensure only one instance of the view exists

        page.views.append(full_page_ui)  # ✅ Add the new page
        page.update()
        page.go("/table_generator")  # ✅ Properly navigate

        # ✅ Fetch courses after UI is ready
        threading.Thread(target=fetch_courses, daemon=True).start()



#     # With this new ElevatedButton:
#     table_generator_btn = ft.ElevatedButton(
#     text="+",    
#     on_click=lambda e: show_table_generator(page),
#     on_hover=hover_shadow,
#     style=ft.ButtonStyle(
#         shape=ft.RoundedRectangleBorder(radius=20),
#         color=ft.colors.WHITE,
#         bgcolor="#2c3744",
#         side=ft.BorderSide(1, ft.colors.WHITE),  # <<-- White border
#     ),
# )
    
    table_generator_btn = ft.IconButton(
        icon="calendar_month",
        icon_color="#2c3744",
        tooltip="Generate Schedule",
        on_click=lambda e: show_table_generator(page),
    )



    # ✅ Bottom Input Bar Restored
    input_bar = ft.Container(
        content=ft.Row(
            [
                table_generator_btn,
                 user_input,
                ft.IconButton(icon="send", on_click=process_query, icon_color="#2c3744"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor="#f5fbf9",
        padding=ft.padding.symmetric(horizontal=15, vertical=8),
        border=ft.border.only(top=ft.border.BorderSide(1, "#2c3744"))  # Add a white border only on the top
    )

    # ✅ Add the suggestions above the input bar inside the chat section
    layout = ft.Column(
        controls=[
            ft.Container(
                chat_messages,
                expand=True  # ✅ Ensures chat takes up all available space
            ),
            ft.Container(
                suggestions_container,  # ✅ Ensures suggestions appear inside chat
                alignment=ft.alignment.center
            ),
            ft.Container(
                input_bar,  # ✅ Ensures input stays at the bottom
                bgcolor="#f5fbf9",
                padding=ft.padding.symmetric(horizontal=15, vertical=8),
            ),
        ],
        expand=True,  # ✅ Expands the entire layout to take full height
    )

    # Use a Container to set the background image
    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Container(  # Ensures image is centered
                        content=ft.Image(
                            src=uj_logo_path,  # Replace with your actual background image path
                            fit=ft.ImageFit.COVER,  # Covers full background
                            expand=True,
                            opacity=0.3,
                            width=200,  # Increase width
                            height=300
                        ),
                        alignment=ft.alignment.center  # Centers the background image
                    ),
                    ft.Column(
                        controls=[
                            header,
                            layout
                        ],
                        expand=True
                    )
                ]
            ),
            expand=True
        )
    )


#ft.app(target=chatbot_ui)
