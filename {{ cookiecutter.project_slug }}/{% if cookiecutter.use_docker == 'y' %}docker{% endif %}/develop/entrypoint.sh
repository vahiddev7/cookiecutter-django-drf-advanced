#!/bin/sh

echo "Running project ..... "

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py collectstatic --clear --noinput
python manage.py collectstatic --noinput

# Start server
echo "--> Starting web process"
python manage.py runserver 0.0.0.0:8000

echo "The project was implemented very well 😎"
