#!/usr/bin/env bash
# wait-and-run.sh

set -e

sleep 10

python3 manage.py migrate && \
exec python3 manage.py runserver 0.0.0.0:8000

