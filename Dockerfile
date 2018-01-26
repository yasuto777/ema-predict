FROM python:alpine

WORKDIR /usr/src/app
RUN pip install Flask && \
        apk update && \
        apk add curl && \
        rm -rf /var/cache/apk/*
