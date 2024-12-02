## How to use

## Installation

1. Install `python3` and poetry:
   ```
   pipx install poetry
   ```
2. Install poetry:
   ```
   poetry install
   ```
3. Run `poetry run python manage.py migrate`
4. Run `poetry run python manage.py createsuperuser --username me --email me@mymail.de`
5. Create file `mysite/.env`:
   ```
   cp mysite/env.sample mysite/.env 
   ```
   and change according to your needs.
6. Create a file `logfile.log` in the main directory:
   ```
   touch logfile.log
   ```
7. Run development server
   ```
   poetry run python manage.py runserver
   ```  
8. The backend can be reached via http://localhost:8000/api/admin   