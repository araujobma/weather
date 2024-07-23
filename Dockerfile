FROM python:3.11.3-slim-buster

COPY ./main.py /app/
COPY ./requirements.txt /app/requirements.txt
COPY ./worker.py /app/worker.py
COPY ./cities.py /app/cities.py
COPY alembic /app/alembic
COPY ./alembic.ini /app/alembic.ini
COPY ./model.py /app/model.py
COPY ./sdk.py /app/sdk.py

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN mkdir /app/logs/

WORKDIR /app

EXPOSE 8080