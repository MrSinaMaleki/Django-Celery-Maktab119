#!/bin/sh

set -e

echo "Running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "starting command $@"
exec "$@"

