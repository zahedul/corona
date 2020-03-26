FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src

COPY ./wait-for /bin/wait-for
RUN chmod 777 -R /bin/wait-for

RUN adduser -D user
USER user

