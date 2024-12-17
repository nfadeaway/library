#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ./library/fixtures/fixture.json

yarn --cwd /app/frontend install
yarn --cwd /app/frontend build
python manage.py collectstatic --noinput

gunicorn -b 0.0.0.0:8000 main_app.wsgi:application
