#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "db in avvio"

    while ! nc -z db 5432; do
        sleep 0.1
    done

    echo "PostgreSQL started"

    echo "Running Flask Migrations"
    export FLASK_APP=/app/wsgi.py
    flask db init
    flask db migrate
    flask db upgrade


fi

gunicorn --config /app/gunicorn_config.py wsgi:app
