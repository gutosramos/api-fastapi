# syntax=docker/dockerfile:1
FROM python:3.12-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends netcat-openbsd \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 1. dependências e config
COPY app/requirements.txt app/alembic.ini ./
COPY app/alembic ./alembic

# 2. entrypoint (ANTES do código para aproveitar cache)
COPY docker-entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# 3. código fonte
COPY app ./app

# 4. instala pacotes
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
