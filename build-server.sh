#!/bin/bash

[ -z "${BACKEND}" ] && exit 1
[ -z "${REPO}" ] && exit 1

if [ "${BACKEND}" == "mysql" ]; then
    apt-get install -y libmysqlclient-dev || exit 1
fi

if [ "${BACKEND}" == "postgresql" ]; then
    apt-get install -y libpq-dev || exit 1
fi

SOURCE_BIN=mongrey_server_${BACKEND}.py
TARGET_NAME=mongrey-server-${BACKEND}

git clone ${REPO} || exit 1 

cd mongrey || exit 1

pip install -e .[server_${BACKEND}] || exit 1

pip freeze

mkdir -p /code/shared/dist

chown user -R /code/shared/dist

cp -a /code/shared/bin/${SOURCE_BIN} /usr/local/bin/mongrey_bin

su -l user -c "/usr/local/bin/pyinstaller --strip --clean --additional-hooks-dir=/code/shared/hooks --distpath=/code/shared/dist -y -F /usr/local/bin/mongrey_bin --name=${TARGET_NAME}" || exit 1

/code/shared/dist/$TARGET_NAME --help || exit 1

exit 0
