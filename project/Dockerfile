# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/project/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/project/entrypoint.sh

# copy project
COPY . /usr/src/project/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/project/entrypoint.sh"]
