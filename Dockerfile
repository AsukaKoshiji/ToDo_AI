# python3.9のイメージをダウンロード
FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000