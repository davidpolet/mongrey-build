FROM ubuntu:14.04

MAINTAINER <stephane.rault@radicalspam.org>

ENV DEBIAN_FRONTEND noninteractive

#ENV GEVENT_RESOLVER ares

ADD sources.list /etc/apt/sources.list

RUN apt-get update -q -y && \
    apt-get dist-upgrade -y --no-install-recommends && \
    apt-get install -y --no-install-recommends \
     build-essential \
     ca-certificates \
     git \
     curl \
     language-pack-en \
     python-dev \
     fabric

ENV PATH /usr/local/bin:${PATH}
ENV LANG en_US.UTF-8

RUN curl -k -O https://bootstrap.pypa.io/ez_setup.py && python ez_setup.py --insecure && rm -f ez_setup.py setuptools*zip

RUN curl -k -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm -f get-pip.py

RUN useradd -d /home/user -m -s /bin/bash user

RUN pip install cython
RUN pip install gevent
RUN pip install --force-reinstall https://github.com/pyinstaller/pyinstaller/tarball/develop
RUN pip install wheel

WORKDIR /code/

