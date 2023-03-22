FROM python:3.10.10-alpine3.17 as rest-admin-app

RUN mkdir /rest-admin-project
COPY . /rest-admin-project
WORKDIR /rest-admin-project
EXPOSE 8000

RUN apk add --no-cache gcc musl-dev python3-dev
RUN pip install -r requirements.txt
RUN cd /rest-admin-project/rest_project && \
    python manage.py migrate

CMD python /rest-admin-project/rest_project/manage.py runserver
