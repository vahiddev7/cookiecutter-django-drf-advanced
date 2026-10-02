#!/bin/sh
set -e

echo "Running project ....."

python manage.py migrate
python manage.py collectstatic --noinput

echo "--> Starting web process"
exec gunicorn --bind 0.0.0.0:8000 config.wsgi:application
