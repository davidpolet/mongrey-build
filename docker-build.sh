#!/bin/bash

[ -z "${PROJECT_VERSION}" ] && exit 1

REPO=https://github.com/radical-software/mongrey.git
CT_NAME=radical-software/mongrey-build

docker build --rm -t $CT_NAME .

declare -a BACKENDS
BACKENDS[0]="mongo"
BACKENDS[1]="sqlite"
BACKENDS[2]="postgresql"
BACKENDS[3]="mysql"

for BACKEND in ${BACKENDS[@]}; do
    echo "Backend : ${BACKEND}"
    docker run -it --rm -e REPO=${REPO} -e BACKEND=${BACKEND} -v `pwd`:/code/shared ${CT_NAME} /bin/bash /code/shared/build-server.sh 2>server-${BACKEND}.log 1>&2 || exit 1
    docker run -it --rm -e REPO=${REPO} -e BACKEND=${BACKEND} -v `pwd`:/code/shared ${CT_NAME} /bin/bash /code/shared/build-web.sh 2>web-${BACKEND}.log 1>&2 || exit 1
done

docker run -it --rm -e REPO=${REPO} -v `pwd`:/code/shared ${CT_NAME} /bin/bash /code/shared/build-server-all.sh 2>server-all.log 1>&2 || exit 1
docker run -it --rm -e REPO=${REPO} -v `pwd`:/code/shared ${CT_NAME} /bin/bash /code/shared/build-web-all.sh 2>web-all.log 1>&2 || exit 1
docker run -it --rm -e REPO=${REPO} -v `pwd`:/code/shared ${CT_NAME} /bin/bash /code/shared/build-all.sh 2>all.log 1>&2 || exit 1

docker run -it --rm -e REPO=${REPO} -v `pwd`:/code/shared ${CT_NAME} /bin/bash /code/shared/build-migration.sh 2>migration.log 1>&2 || exit 1
