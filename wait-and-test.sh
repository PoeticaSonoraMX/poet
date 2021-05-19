#!/usr/bin/env bash
# wait-and-run.sh

set -e

sleep 10

python3 manage.py test
