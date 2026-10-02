#!/bin/sh
set -e

echo "Running project ....."

python manage.py migrate
python manage.py collectstatic --noinput

echo "--> Starting development server"
exec python manage.py runserver 0.0.0.0:8000
