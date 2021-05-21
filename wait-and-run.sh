#!/usr/bin/env bash
# wait-and-run.sh

set -e

sleep 10

python3 manage.py migrate


if [ "$DEBUG" == "true" ]
then
  python3 manage.py runserver 0.0.0.0:8000
else
  python3 manage.py collectstatic --no-input --clear
  uwsgi --http 0.0.0.0:80 --module config.wsgi
fi
