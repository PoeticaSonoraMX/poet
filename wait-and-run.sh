#!/usr/bin/env bash
# wait-and-run.sh

set -e

sleep 10

python manage.py migrate


if [ "$DEBUG" == "true" ]
then
  python manage.py runserver 0.0.0.0:8000
else
  python manage.py collectstatic --no-input --clear
  uwsgi --ini /home/poet/uwsgi.ini
fi
