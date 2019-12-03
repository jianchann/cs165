FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code/

RUN apk add postgresql-dev
RUN apk --upgrade add libffi-dev build-base 

RUN pip install -r requirements.txt
RUN mkdir /code/app
ADD ./run.py /code/
ADD ./app /code/app/

RUN apk del build-base

ENTRYPOINT python run.py
