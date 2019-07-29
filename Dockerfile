# pull official base image
FROM ubuntu:18.04

# install req for python pillow
RUN apt-get update && apt-get install -y libjpeg-dev python-dev python-setuptools

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH /usr/local/bin:$PATH


FROM python:3.7

# set work directory
WORKDIR /usr/src/backend

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/backend/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/backend/
