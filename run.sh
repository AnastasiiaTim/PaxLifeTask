#!/bin/bash

apt-get update && apt-get install -y --no-install-recommends \
python3.6 python-pip python3-pip python3-setuptools mysql-server python3.6-dev libmysqlclient-dev
&& apt-get clean \
&& pip3 install virtualenv
&& virtualenv --python=python3.6 flights_venv
source flights_venv/bin/activate &&
pip3 install django==1.10.6 &&
python manage.py runserver 127.0.0.1:8000

