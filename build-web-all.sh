#!/bin/bash

[ -z "${REPO}" ] && exit 1

SOURCE_BIN=mongrey_web.py
TARGET_NAME=mongrey-web

apt-get install -y libpq-dev
apt-get install -y libmysqlclient-dev

git clone ${REPO} || exit 1 

cd mongrey || exit 1

pip install -e .[web]

mkdir -p /code/shared/dist

chown user -R /code/shared/dist

cp -a /code/shared/bin/${SOURCE_BIN} /usr/local/bin/mongrey_bin

su -l user -c "/usr/local/bin/pyinstaller --strip --clean --additional-hooks-dir=/code/shared/hooks --distpath=/code/shared/dist -y -F /usr/local/bin/mongrey_bin --name=${TARGET_NAME}" || exit 1

/code/shared/dist/$TARGET_NAME --help || exit 1

exit 0
