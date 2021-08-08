FROM python:3.8.6-alpine

ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN mkdir "/app"
COPY test_docker /app
WORKDIR /app