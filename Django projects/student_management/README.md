Student Management System (Django)

Setup (PowerShell):

1) Create and activate venv;
   python -m venv .venv; .\.venv\Scripts\Activate.ps1
2) Install requirements;
   pip install -r requirements.txt
3) Run migrations;
   python manage.py migrate
4) Create superuser (optional);
   python manage.py createsuperuser
5) Run server;
   python manage.py runserver

Project structure: students app with models: Course, Student, Marks.
