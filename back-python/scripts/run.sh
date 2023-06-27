#!/bin/sh

set -e

#python manage.py wait_for_db

#python manage.py collectstatic --noinput

#uwsgi --socket :9000 --workers 4 --master --enable-threads --module sistemia.wsgi:application

#APP_PORT=${APP_PORT:-8000}

#gunicorn sistemia.wsgi:application -w 2 --bind "0.0.0.0:${APP_PORT}"

python manage.py runserver 0.0.0.0:8000

