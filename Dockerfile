FROM python:3.11.3-slim-buster

COPY ./main.py /app/
COPY ./requirements.txt /app/requirements.txt
COPY ./worker.py /app/worker.py

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN mkdir /app/logs/

WORKDIR /app

EXPOSE 8080