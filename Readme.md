## py-django-mongo
## simple python django template using mongo


This is just a simple template web service I use when I need to spin up a quick document or rest server using django

### Setup

Download the repo and run 
```shell
pip install 
```

#### initialize the db

```shell
python manage.py seed_users
```

#### run
The server will default to port 8000. If you want to set a different port, set the `DJANGO_RUNSERVER_PORT` environment variable

```shell
export DJANGO_RUNSERVER_PORT=4000
python manage.py 
```