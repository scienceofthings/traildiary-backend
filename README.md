## How to use

The backend can be reached via http://localhost:8000/api/admin

## Installation

1. Install `python3` and `python3-venv`
2. Create virtual env directory (with IntelliJ or command line `python3 -m venv venv`)
3. Run `source venv/bin/activate`
4. Run `pip install -r requirements.txt`
5. Run `python mysite/manage.py makemigrations traildiary`
6. Run `python mysite/manage.py migrate`   
5. Run `python mysite/manage.py createsuperuser --username me --email me@mymail.de`
6. Create file `mysite/.env`
7. Rename `mysite/env.sample` to `mysite/.env` and change according to your needs.
8. Create a file `logfile.log` in the main directory
9. For development server: Run `python manage.py runserver` in the main directory