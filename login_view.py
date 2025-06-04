import flet as ft
from auth import sign_in, sign_up, reset_password
from chatbot_view import chatbot_ui  # Import chatbot UI function


def main(page: ft.Page):
    page.title = "UniGuide"
    page.theme_mode = ft.ThemeMode.LIGHT  # Keep it modern
    page.bgcolor = "#F8F9FA"  # Light gray background for a clean look

    # ✅ FIXED WINDOW SETTINGS
    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False
    page.padding = 0


    # ✅ HOME PAGE (Welcome Screen)
    def home_page():
        page.clean()

        welcome_text = ft.Text("Welcome to\nUniGuide Chatbot", size=20, weight=ft.FontWeight.BOLD, text_align="center")

        logo = ft.Container(
        content=ft.Image(
            src=r"C:\Users\Asus\OneDrive - AmberX\JU\graduation project 3\Design pages\logo.jpg",  # Update with your image path
            fit=ft.ImageFit.CONTAIN,
            width=300,
            height=300
        ),
        alignment=ft.alignment.top_center,
        margin=ft.margin.only(top=50)
    )

        sign_up_btn = ft.ElevatedButton(
            text="Sign Up",
            width=250,
            bgcolor="#002147",
            color="white",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
            on_click=lambda e: sign_up_page()
        )

        login_btn = ft.ElevatedButton(
            text="Log In",
            width=250,
            bgcolor="#3B4D61",
            color="white",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
            on_click=lambda e: login_page()
        )

        page.add(
            ft.Column(
                controls=[logo, welcome_text, sign_up_btn, login_btn],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    # ✅ LOGIN PAGE
    def login_page():
        page.clean()

        # 🔥 Background Logo (Fully Centered & Faded)
        background_logo = ft.Container(
            content=ft.Image(
                src=r"C:\Users\Asus\OneDrive - AmberX\JU\graduation project 3\Design pages\logo.jpg",  # Update your path
                fit=ft.ImageFit.CONTAIN,  # Ensures it remains within the screen
                opacity=0.2,  # Faded effect
                width=500,  # Adjust width for better centering
                height=500   # Adjust height for full visibility
            ),
            alignment=ft.alignment.center,  
            margin=ft.margin.only(top=50)  # Moves logo slightly down
        )

        # 🟢 Login Form Inputs
        email_input = ft.TextField(
            hint_text="Username",
            border_radius=ft.border_radius.all(25),
            bgcolor="white",
            color="black",
            width=320,
            prefix_icon="email"
        )

        password_input = ft.TextField(
            hint_text="Password",
            password=True,
            border_radius=ft.border_radius.all(25),
            bgcolor="white",
            color="black",
            width=320,
            prefix_icon="lock"
        )

        error_message = ft.Text("", color="red", size=14, text_align=ft.TextAlign.CENTER)

        # 🔹 Handle Login Function
        def handle_login(e):
            email = email_input.value.strip()
            password = password_input.value.strip()

            if not email or not password:
                error_message.value = "⚠️ Please enter both username and password!"
                page.update()
                return

            user_id = sign_in(email, password)

            if user_id:
                page.clean()
                chatbot_ui(page, user_id, home_page)  # ✅ Redirects to chatbot
            else:
                error_message.value = "❌ Invalid email or password!"
                page.update()

                # 🔹 Handle Forgot Password Function
        def handle_forgot_password(e):
            email = email_input.value.strip()
            if not email:
                error_message.value = "⚠️ Please enter your email to reset password!"
                page.update()
                return

            success = reset_password(email)
            if success:
                error_message.value = "✅ Password reset email sent! Check your inbox."
            else:
                error_message.value = "❌ Error sending reset email."
            page.update()

        # 🔵 Login Form UI (Further Lowered)
        login_form = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Log in", size=22, weight=ft.FontWeight.BOLD, text_align="center"),
                    email_input,
                    password_input,
                    ft.ElevatedButton(
                        text="SUBMIT",
                        width=320,
                        bgcolor="#002147",
                        color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
                        on_click=handle_login  
                    ),
                    error_message,
                    ft.TextButton(
                        text="Forgot Password?",
                        style=ft.ButtonStyle(color="blue"),
                        on_click=handle_forgot_password
                    ),
                    ft.TextButton(
                        text="Don't have an account? Sign Up Here",
                        style=ft.ButtonStyle(color="#002147"),
                        on_click=lambda e: sign_up_page()
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=250)  
        )

        # ✅ Stack UI
        page.add(
            ft.Stack(
                controls=[background_logo, login_form]
            )
        )




    # ✅ SIGN UP PAGE
    def sign_up_page():
        page.clean()

        # 🔥 Background Logo (Fully Centered & Faded)
        background_logo = ft.Container(
            content=ft.Image(
                src=r"C:\Users\Asus\OneDrive - AmberX\JU\graduation project 3\Design pages\logo.jpg",  # Update your path
                fit=ft.ImageFit.CONTAIN,  # Ensures it remains within the screen
                opacity=0.2,  # Faded effect
                width=500,  # Adjust width for better centering
                height=500   # Adjust height for full visibility
            ),
            alignment=ft.alignment.center,  
            margin=ft.margin.only(top=50)  # Moves logo slightly down
        )

        # 🟢 Input Fields for Sign-Up
        first_name = ft.TextField(hint_text="First Name", border_radius=25, bgcolor="white", width=320)
        last_name = ft.TextField(hint_text="Last Name", border_radius=25, bgcolor="white", width=320)
        email = ft.TextField(hint_text="Email", border_radius=25, bgcolor="white", width=320)
        password = ft.TextField(hint_text="Password", password=True, border_radius=25, bgcolor="white", width=320)
        confirm_password = ft.TextField(hint_text="Confirm Password", password=True, border_radius=25, bgcolor="white", width=320)

        error_message = ft.Text("", color="red", size=14, text_align=ft.TextAlign.CENTER)

        # 🔹 Handle Sign-Up Logic
        def handle_signup(e):
            if not first_name.value.strip() or not last_name.value.strip() or not email.value.strip() or not password.value.strip() or not confirm_password.value.strip():
                error_message.value = "⚠️ All fields are required!"
                page.update()
                return

            if password.value != confirm_password.value:
                error_message.value = "❌ Passwords do not match!"
                page.update()
                return

            user_id = sign_up(email.value.strip(), password.value.strip())
            if user_id:
                error_message.value = "✅ Account created successfully! Now sign in."
            else:
                error_message.value = "❌ Error creating account."
            page.update()

        # 🔵 Sign-Up Form UI (Lowered)
        sign_up_form = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Sign Up", size=22, weight=ft.FontWeight.BOLD, text_align="center"),
                    first_name,
                    last_name,
                    email,
                    password,
                    confirm_password,
                    ft.ElevatedButton(
                        text="Sign Up",
                        width=320,
                        bgcolor="#002147",
                        color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
                        on_click=handle_signup  # ✅ Calls the function inside `sign_up_page`
                    ),
                    ft.Text(
                        "By clicking the Sign Up button, you agree to our Terms and Conditions and Privacy Policy.",
                        size=12,
                        text_align="center"
                    ),
                    ft.TextButton(
                        text="Already have an account? Log In Here",
                        style=ft.ButtonStyle(color="#002147"),
                        on_click=lambda e: login_page()
                    ),
                    error_message
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=150)  # ⬇️ Moves the form even lower
        )

        # ✅ Stack to Overlay Form on Background
        page.add(
            ft.Stack(
                controls=[background_logo, sign_up_form]
            )
        )

    home_page()  # Load home page on startup


ft.app(target=main)
