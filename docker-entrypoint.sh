#!/bin/sh
set -e

echo "⏳ Waiting for Postgres at $DB_HOST:$DB_PORT..."

until nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 1
done

echo "✅ Postgres is up"

echo "📦 Running Alembic migrations..."
cd /app
alembic upgrade head

echo "🚀 Starting FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
