import firebase_admin
from firebase_admin import credentials, auth, db
import requests
import webbrowser

# ✅ Load Firebase credentials
cred = credentials.Certificate("")  # Ensure correct path
firebase_admin.initialize_app(cred, {
    'databaseURL': ''  # Replace with your Firebase URL
})

# 🔥 Firebase Web API Key (Replace with yours)
FIREBASE_WEB_API_KEY = ""

# 🔥 Facebook App Credentials (Replace with yours)
FACEBOOK_APP_ID = ""
FACEBOOK_APP_SECRET = ""

def sign_up(email, password):
    """Create a new user in Firebase Authentication."""
    try:
        user = auth.create_user(email=email, password=password)
        return user.uid
    except firebase_admin.exceptions.FirebaseError as e:
        print(f"❌ Error signing up: {e}")
        return None

def sign_in(email, password):
    """Authenticate user using Firebase REST API."""
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
    data = {"email": email, "password": password, "returnSecureToken": True}
    
    response = requests.post(url, json=data)
    result = response.json()

    if "idToken" in result:
        user_id = result["localId"]  # Unique user ID from Firebase
        return user_id
    else:
        print(f"❌ Error signing in: {result.get('error', {}).get('message', 'Unknown error')}")
        return None

def reset_password(email):
    """Send a password reset email."""
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_WEB_API_KEY}"
    data = {"requestType": "PASSWORD_RESET", "email": email}

    response = requests.post(url, json=data)
    result = response.json()

    if "email" in result:
        print("✅ Password reset email sent successfully!")
        return True
    else:
        print(f"❌ Error sending password reset email: {result.get('error', {}).get('message', 'Unknown error')}")
        return False

# 🔥 **Save Chats Per User**
def load_chat_history(user_id):
    """Load chat history for a specific user from Firebase."""
    if not user_id:
        print("⚠️ No user ID provided. Cannot load chats.")
        return []
    
    try:
        ref = db.reference(f"/users/{user_id}/chats")  # 🔥 Load from /users/user_id/chats
        history = ref.get()
        if history is None:
            history = []  # Return empty list if no chat history exists
        print(f"✅ Chat history loaded successfully for user: {user_id}")
        return history
    except Exception as e:
        print(f"❌ Error loading chat history: {e}")
        return []


# 🔥 **Load Chats Per User**
def load_chat_history(user_id):
    """Load chat history for a specific user from Firebase."""
    if not user_id:
        print("⚠️ No user ID provided. Cannot load chats.")
        return []
    
    try:
        ref = db.reference(f"/users/{user_id}/chats")  # 🔥 Load from /users/user_id/chats
        history = ref.get()
        if history is None:
            history = []  # Return empty list if no chat history exists
        print(f"✅ Chat history loaded successfully for user: {user_id}")
        return history
    except Exception as e:
        print(f"❌ Error loading chat history: {e}")
        return []



# 🔥 Updated Facebook Login - OAuth Flow
def sign_in_facebook():
    """Sign in with Facebook via Firebase OAuth."""
    facebook_url = f"https://www.facebook.com/v12.0/dialog/oauth?client_id={FACEBOOK_APP_ID}&redirect_uri=https://your-project-id.firebaseapp.com/__/auth/handler&scope=email"

    # ✅ Open the login page in the browser
    webbrowser.open(facebook_url)
    print("🌍 Facebook sign-in opened in browser. After login, Firebase will handle authentication.")


# 🔥 Social Login (OAuth - Firebase)
def sign_in_google():
    """Sign in with Google (OAuth)."""
    print("⚠️ Google Sign-in is not implemented yet. Use Firebase Auth SDK for OAuth.")


def sign_in_apple():
    """Sign in with Apple (OAuth)."""
    print("⚠️ Apple Sign-in is not implemented yet. Use Firebase Auth SDK for OAuth.")
