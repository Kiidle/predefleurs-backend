#!/bin/sh
set -o errexit
set -o pipefail
set -o nounset

export PGPASSWORD=pw_tradesync.db.2023
until psql -h db -U tradesync_db_admin -d tradesync_database -w -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python manage.py migrate --noinput
exec "$@"