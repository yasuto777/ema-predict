FROM python:alpine

WORKDIR /usr/src/app
RUN apk update && \
        apk add curl build-base && \
        rm -rf /var/cache/apk/* && \
        pip install \
                Werkzeug \
                requests \
                Flask \
                Flask-Sockets \
                eventlet \
                greenlet \
                gevent \
                gunicorn
