#!/bin/sh
set -e

echo "Running project ....."

export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-config.settings.prod}"

python manage.py migrate
python manage.py collectstatic --noinput

echo "--> Starting web process"
exec gunicorn --bind 0.0.0.0:8000 config.wsgi:application
