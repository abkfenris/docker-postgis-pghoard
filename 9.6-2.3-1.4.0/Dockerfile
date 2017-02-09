FROM mdillon/postgis:9.6
MAINTAINER Alex Kerney <abk@mac.com>

RUN apt-get update && apt-get install -y \
  python3 \
  python3-dev \
  python3-psycopg2 \
  python3-cryptography \
  libsnappy-dev \
  postgresql-server-dev-9.6 \
  libffi-dev \
  libssl-dev \
  gcc \
  unzip

ADD https://bootstrap.pypa.io/get-pip.py /opt/get-pip.py
RUN python3 /opt/get-pip.py

RUN pip install \
  boto==2.45.0 \
  httplib2==0.10.3 \
  google-api-python-client==1.6.2 \
  'oauth2client<4.0.0' \
  azure==1.0.3

ADD https://pghoard.ohmu.fi/debian/python3-snappy_0.5-1_amd64.deb /opt/python3-snappy.deb
RUN dpkg -i /opt/python3-snappy.deb
RUN apt-get install -f -y

ADD https://github.com/ohmu/pghoard/archive/master.zip /opt/pghoard.zip
RUN unzip /opt/pghoard.zip
RUN python3 /pghoard-master/setup.py bdist_egg
RUN easy_install /pghoard-master/dist/pghoard-1.4.0-py3.4.egg

RUN mkdir /backups

ENTRYPOINT ["/docker-entrypoint.sh"]

COPY ./initdb-pghoard.sh /docker-entrypoint-initdb.d/initdb-pghoard.sh

EXPOSE 5432
CMD ["postgres"]
