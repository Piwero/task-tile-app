# Tiles and tasks app with Django 2.2.24

## Getting started:

---
This app allows user to create, read, update and delete tasks. These tasks are group together in containers called tiles.

##Set up

---
In order to run this project, clone this repository on you local. Then, follow the following steps:

### Create and activate virtualenv
```commandline
virtualenv .venv -p python3
. .venv/bin/activate
```

### Install requirements
```commandline
pip install Poetry
poetry install
```

### Secret keys
python-decouple has been used for hiding secrets and keys of this project. You can create a local .env file with the following command and structure.

```commandline
touch .env
```
**.env**:
```
# Django Secrets

SECRET_KEY = "" # to be provided by piwero
```
### Run migrations to create models in a SQL DB.
```commandline
python manage.py migrate
```
## Run server

#### Backend
```commandline
python manage.py runserver
```

### Run tests

#### Backend
```commandline
python manage.py tests
```
### API documentation
```djangourlpath
localhost:8000/api/schema/swagger-ui/

localhost:8000/api/schema/redoc/
```
---
