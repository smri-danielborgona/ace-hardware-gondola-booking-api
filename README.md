# Django Rest Framework Project

## Installation
Requires `python 3.11`

```shell
python -m virtualenv venv
venv\scripts\activate  # activate virtual environment
pip install -r requirements.txt
```

## Apply migrations
Make sure you are in your virtual environment. To activate your virtual environment, run the following command: `venv\scripts\activate` (Windows)
```bash
python manage.py migrate
```

## Create a superuser
```bash
python manage.py createsuperuser
```

## Run Local Server
```bash
python manage.py runserver
```

## Running tests
```bash
python manage.py test
```
