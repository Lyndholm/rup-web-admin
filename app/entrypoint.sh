#!/bin/sh

set -eu

postgres_ready() {
    python <<END
import sys

import psycopg

try:
    psycopg.connect(
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
    )
except psycopg.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}

until postgres_ready; do
    echo >&2 "Waiting for PostgreSQL to become available..."
    sleep 1
done
echo >&2 "PostgreSQL is available"

if [ "$DEBUG" = "0" ]; then
    echo "Starting django app in PROD mode"

    python manage.py migrate --no-input
    python manage.py collectstatic --noinput --clear
    gunicorn core.wsgi:application --bind 0.0.0.0:8000
elif [ "$DEBUG" = "1" ]; then
    echo "Starting django app in DEBUG mode"

    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
fi

exec "$@"
