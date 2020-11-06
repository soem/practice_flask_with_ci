FROM python:3.9-alpine

RUN \
    pip install flask && \
    pip install sqlalchemy && \
    apk add --no-cache \
        gcc musl-dev postgresql-dev && \
    pip install psycopg2

COPY user_crud /app/user_crud

CMD ["python", "/app/user_crud/api.py"]
