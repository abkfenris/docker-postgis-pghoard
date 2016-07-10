FROM mdillon/postgis:9.3
MAINTAINER Alex Kerney <abk@mac.com>

RUN apt-get update && apt-get install -y \
  python3 \
  python3-dev \
  python3-pip \
  libsnappy-dev \
  postgresql-server-dev-9.3 \
  libffi-dev
RUN pip3 install boto httplib2 google-api-python-client

ADD https://github.com/ohmu/pghoard/archive/1.2.0.tar.gz pghoard.tar.gz
RUN tar xzf pghoard.tar.gz
RUN python3 pghoard-1.2.0/setup.py bdist_egg
RUN easy_install3 pghoard-1.2.0/dist/pghoard-1.2.0-py3.4.egg

RUN mkdir /backups

COPY ./docker-entrypoint.sh /
