FROM python:3.6.8-alpine3.9



ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD requirements.txt /var/www/
RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD . /var/www/


RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:application"]

