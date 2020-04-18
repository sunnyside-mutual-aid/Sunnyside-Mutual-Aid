# Sunnyside-Mutual-Aid
This is the repo for the Sunnyside Mutual Aid Website.

## Technology used
### Production
===========================================================================
1. **Web**: Django
+ Django is an open source Python-based web framework for rapid development.
+ **Tutorial**: https://www.tutorialspoint.com/django/index.htm

2. **WSGI**: Gunicorn

3. **DB**: PostgreSQL
+ PostgreSQL is an open source Relational Database System.The DB is primarily accessed through Django.
+ **Tutorial**: https://www.tutorialspoint.com/postgresql/index.htm
+ **Tutorial (Django and DBs)**: https://www.tutorialspoint.com/django/django_models.htm

4. **Web Server**: nginx

5. **Certificate renewal**: certbot

6. **Containerization**: Docker and Docker Compose
+ **Tutorial**: https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial

7. **Front-end**: Bootstrap, Font-Awesome
+ Bootstrap tutorial: https://www.w3schools.com/bootstrap4
+ Font-Awesome tutorial: https://www.w3schools.com/icons/fontawesome5_intro.asp

### Development
===========================================================================
The development environment is slimmed down to 2 containers:
1. Web
2. DB

It uses Django's manage.py for WSGI, and runs on localhost:8000


### Spinning up your own development environment
===========================================================================
1. Clone/Download this repo.
2. Install Docker and Docker Compose.
3. Run `docker-compose up -d --build`
4. Go to localhost:8000 in your web browser.

That's it! All the HTML pages are in `project/website/templates/` directory. To add new pages, please add them here and update urls.py.
Static content goes in the `project/static/` directory, and is collected when you run 

+ `docker-compose up -d --build` or 
+ `docker-compose exec web python manage.py collectstatic --no-input`

