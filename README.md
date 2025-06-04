# 🧠 UniGuide: Intelligent Virtual Assistant for the University of Jordan

UniGuide is a multilingual Intelligent Virtual Assistant designed to help students, academic staff, and administrative departments at the University of Jordan access essential information quickly and easily. It enhances the university experience by providing 24/7 access to course schedules, campus navigation, academic resources, and more—all through a smart, conversational interface.

---![Screenshot 2025-06-04 165903](https://github.com/user-attachments/assets/37a7de0e-28b2-4be5-8fb0-24826ee379cb)


## 🚀 Key Features

- 🔍 **Smart Search & Q&A**: Ask about course details, registration dates, prerequisites, and receive instant answers.
- 🌐 **Multilingual Support**: Interact in Arabic and English (more coming soon).
- 📅 **Course Schedule Generator**: Create and manage your personalized schedule directly within the chat.
- 🗺️ **Campus Navigation**: Integrated with Google Maps API for building directions and location help.
- 🧾 **Admin Dashboard**: Secure portal to manage courses, student records, and chatbot content.
- 🔐 **Secure Login**: Authentication and encrypted communication for user data protection.
- 📈 **Usage Analytics**: Track most asked questions and system performance for continual improvement.
- 🧠 **Real-Time Updates**: Connected to the university database for the latest academic info.

---

## 🛠️ Tech Stack

| Layer          | Technology Used |
|----------------|-----------------|
| Frontend       | Flet (Python-based UI) |
| Backend        | Python, Firebase Functions, Pinecone API |
| Database       | Firebase (Realtime DB), Pinecone (Vector DB), SQLite (Local DB) |
| API Integrations | Google Maps API |

---

![Screenshot 2025-06-04 170034](https://github.com/user-attachments/assets/98c48f0d-6fcf-4834-980e-5c6e8f995f4d)

---


## 📦 Installation

### Prerequisites
- Python 3.10+
- Firebase credentials (`firebase_config.json`)
- Pinecone API Key
- VS Code (recommended)

### Local Setup
```bash
git clone https://github.com/YOUR_USERNAME/UniGuide.git
cd UniGuide
pip install -r requirements.txt
python login_view.py
