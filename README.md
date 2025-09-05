# CookChiefs — Django + SQLite

A clean, modern recipes web app with login/signup and CRUD for recipes.

## Quickstart

1) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

2) Install Django
```bash
pip install django
```

3) Run migrations & start the dev server
```bash
python manage.py migrate
python manage.py runserver
```

4) Open http://127.0.0.1:8000/ — Sign up, log in, and start adding recipes!

## Admin
Create a superuser to access /admin
```bash
python manage.py createsuperuser
```

## Notes
- Uses Django auth + SQLite3 (no external DB needed).
- Templates are pure HTML5 + CSS (no external frameworks).
- Edit/delete recipes is limited to the author.
