FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code && \
    mkdir -p /code/public/static && \
    mkdir -p /code/public/media

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY backend /code/

WORKDIR /code/

EXPOSE 8080
