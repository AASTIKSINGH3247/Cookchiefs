# CookChiefs — Django + SQLite

CookChiefs is a clean, modern web application for sharing and managing recipes. Users can sign up, log in, create, read, update, and delete their own recipes. Built with **Django** and **SQLite**, this app is simple, lightweight, and easy to use.

---

## Features

- User authentication: Sign up, log in, and log out.
- CRUD operations for recipes (Create, Read, Update, Delete).
- Recipes are private to their authors (edit/delete restricted).
- Clean HTML5 + CSS templates (no external frameworks required).
- Built-in Django admin for easy management.

---

## Screenshots

### Login Page
![Login Page]
|--------------------------|


Users can log in with their account credentials or navigate to the signup page.

### Signup Page
![Signup Page](screenshots/signup.png)  
New users can create an account in a few simple steps.

### Home Page
![Home Page](screenshots/home.png)  
After logging in, users see a list of all recipes. Authors see edit/delete options for their own recipes.

### Recipe Detail / Working Page
![Recipe Page](screenshots/recipe.png)  
Click on a recipe to view details, and edit or delete if you are the author.

---

## Quickstart

1. **Create and activate a virtual environment (recommended)**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

2.Install Django

pip install django


Run migrations & start the development server

python manage.py migrate
python manage.py runserver


Open in browser
Navigate to http://127.0.0.1:8000/
 — sign up, log in, and start adding recipes!

Admin Panel

Create a superuser to access the Django admin panel at /admin:

python manage.py createsuperuser

Notes

Uses Django authentication + SQLite3 (no external database required).

Templates are pure HTML5 + CSS, easy to customize.

Only recipe authors can edit or delete their recipes.

Optional Improvements

Add recipe categories or tags.

Include search and filter functionality.

Enhance UI with a CSS framework (Bootstrap/Tailwind).

Add image upload for recipes.
