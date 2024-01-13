#!/bin/bash

if [ $EUID == 0 ] ; then
    echo "You are root! Please, run me as a normal user."
    exit 1
fi

WD=$(dirname "$(realpath "$0")")
SITE_DATA="$WD/site"

mkdir -p "$SITE_DATA" >/dev/null 2>&1

CONTAINER_NAME="lucaph"
docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME

# docker run \
#     --rm \
#     --name=$CONTAINER_NAME \
#     --network=bridge \
#     -p 1409:1409 \
#     --mount type=bind,source=$SITE_DATA,target=/site \
#     luca/jekyll_dev jekyll new .


# docker run \
#     -it \
#     --rm \
#     --name=$CONTAINER_NAME \
#     --network=bridge \
#     -p 1409:1409 \
#     --mount type=bind,source=$SITE_DATA,target=/site \
#     luca/jekyll_dev jekyll serve -H 0.0.0.0 -P 1409

docker run \
    -it \
    --rm \
    --name=$CONTAINER_NAME \
    --network=bridge \
    -p 1409:1409 \
    --mount type=bind,source=$SITE_DATA,target=/site \
    luca/jekyll_dev /bin/bash
