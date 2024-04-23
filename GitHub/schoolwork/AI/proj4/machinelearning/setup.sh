#!/usr/bin/env bash

apt-get update
apt-get install software-properties-common
add-apt-repository ppa:deadsnakes/ppa

apt-get install -y python3.9 python3.9-distutils python3-pip python3-dev libtiff5-dev libjpeg8-dev \
libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev \
tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev

python3.9 -m pip install --upgrade setuptools
python3.9 -m pip install --upgrade pip
python3.9 -m pip install --upgrade distlib
python3.9 -m pip install --upgrade numpy
python3.9 -m pip install --upgrade matplotlib
python3.9 -m pip install -r /autograder/source/requirements.txt