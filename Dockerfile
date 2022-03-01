FROM python:3.9.10-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y make

COPY ./requirements.txt .
COPY ./requirements-pip.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-pip.txt

RUN useradd -u 8877 user
USER user
