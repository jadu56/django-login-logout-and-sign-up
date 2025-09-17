# Django User Authentication Project

This is a simple **Django web project** that integrates **user registration, login, and logout functionalities** into a single app.  
It uses **django-crispy-forms with Bootstrap 5** for clean and responsive UI.

---

## ✨ Features
- User **Registration** with:
  - Username
  - Email
  - First Name & Last Name
  - Password & Confirm Password
- User **Login / Logout**
- Redirect to **Home Page** after login/logout
- Navbar that changes depending on authentication status
- Beautiful UI with **Bootstrap 5 + Crispy Forms**

---

## ⚙️ Installation

1. **Clone the project**
   ```bash
   git clone https://github.com/yourusername/django-auth-project.git
   cd django-auth-project
2.Create a virtual environment
  python -m venv .venv
  source .venv/bin/activate    # On Linux / Mac
  .venv\Scripts\activate       # On Windows
3.Install dependencies
  pip install -r requirements.txt
Or install manually:   
  pip install django django-crispy-forms crispy-bootstrap5
4.Run migrations:
  python manage.py migrate
5.Create a superuser (admin):
  python manage.py createsuperuser
6.Start the server
  python manage.py runserver
7.Open in browser:
  http://127.0.0.1:8000/
📂 Project Structure

      mysite/
    │── accounts/           # App for user registration & login
    │   ├── views.py
    │   ├── forms.py
    │   └── urls.py
    │
    │── mysite/             # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │── templates/
    │      ├──accounts/
    │      │     └──register.html
    │      ├──registration/
    │      │       └──login.html
    │      ├── base.html
    │      ├──home.html
    │      ├──profile.html
    │
    │──static/
    │
    │── manage.py
    │── requirements.txt
    │── README.md
📦 Dependencies
     
    Python 3.10+
    
    Django 5.2+
    
    django-crispy-forms
    
    crispy-bootstrap5

🚀 Usage

    Visit /accounts/register/ → Create a new account
    
    Visit /accounts/login/ → Login with username & password
    
    Use the Logout button to sign out
    
    Homepage displays different UI for logged in vs guest users

📸 Screenshots
   
    Register Page
    
    Login Page

🔗 Useful Links

    Django Documentation
    
    django-crispy-forms
    
    Bootstrap 5

