## Installation for development

1. Install `python3` and `python3-venv`
2. Create virtual env directory (with IntelliJ or command line `python3 -m venv venv`)
3. Run `source venv/bin/activate`
4. Run `pip install -r requirements.txt`
5. Run `python mysite/manage.py makemigrations traildiary`
6. Run `python mysite/manage.py migrate`   
5. Run `python mysite/manage.py createsuperuser --username me --email me@mymail.de`

## Installation for production

Additionally, to installation for development:

1. Change variables in `settings.py`: 
   - `SECRET_KEY`
   - `DEBUG`
   - `ALLOWED_HOSTS`
   - `SECURE_SSL_REDIRECT`
   - `SESSION_COOKIE_SECURE`
   - `CSRF_COOKIE_SECURE`