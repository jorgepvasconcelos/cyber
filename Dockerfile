FROM python:3.11-slim-buster

# install dependencies
COPY ./requirements.txt /var/www/requirements.txt
WORKDIR /var/www
RUN pip install -r requirements.txt

COPY . /var/www
WORKDIR /var/www

# ENVS
ENV PYTHONPATH "${PYTHONPATH}:/var/www/src"
