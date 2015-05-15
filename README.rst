=============
Mongrey Build
=============

Auto build for `Mongrey Project: <https://github.com/radical-software/mongrey>`_

Build Process
=============

1. Make Docker image for all builds
2. Run docker contenair
3. By package (mongodb, postgresql, web, server, ...):
    1. Clone Mongrey Project

Run Build
=========

::

    git clone https://github.com/radical-software/mongrey-build

    # mongrey release  
    $ export PROJECT_VERSION=0.4.1

    $ ./docker-build.sh
    
Upload Project to remote host
=============================

::

    # Host for upload binaries by fabric/ssh
    $ export FABRIC_REMOTE_HOST=YOUR_HOST
    
    # SSH password for remote host
    $ export FABRIC_REMOTE_PASSWORD=YOUR_SSH_PASSWORD

    # Remote path
    $ export FABRIC_REMOTE_PATH=/home/download

    $ docker run -it --rm -v `pwd`:/code \
        -e PROJECT_VERSION=$PROJECT_VERSION \
        -e FABRIC_REMOTE_HOST=$FABRIC_REMOTE_HOST \
        -e FABRIC_REMOTE_PATH=$FABRIC_REMOTE_PATH \
        -e FABRIC_REMOTE_PASSWORD=$FABRIC_REMOTE_PASSWORD \
        -w /code radical-software/mongrey-build fab upload

TODO
====

- Travis Tests
- Nightly build for master branch
- build by tag
