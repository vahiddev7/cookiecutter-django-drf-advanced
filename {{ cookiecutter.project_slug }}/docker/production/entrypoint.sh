#!/bin/sh

echo "Running project ..... "

python manage.py migrate
python manage.py collectstatic --clear --noinput
python manage.py collectstatic --noinput

echo "--> Starting web process"
gunicorn --bind 0.0.0.0:8000 config.wsgi:application

echo "The project was implemented very well 😎"
