#!/bin/bash
set -e

echo "⏳ Aguardando Postgres em ${DB_HOST:-db}:${DB_PORT:-5432}..."
while ! nc -z ${DB_HOST:-db} ${DB_PORT:-5432}; do sleep 0.5; done
echo "✅ Postgres respondendo"

echo "📦 Alembic upgrade head"
alembic -c /app/alembic.ini upgrade head

echo "🚀 Iniciando FastAPI"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
