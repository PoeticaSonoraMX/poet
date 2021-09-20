#!/usr/bin/env bash
# wait-and-test.sh

set -e

sleep 10

python manage.py test
