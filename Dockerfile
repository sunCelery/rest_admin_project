FROM python:3.10.10-alpine3.17 as rest-admin-app

RUN mkdir /rest-admin-project
COPY . /rest-admin-project
WORKDIR /rest-admin-project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache gcc musl-dev python3-dev build-base linux-headers
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
