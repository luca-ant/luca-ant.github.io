#!/bin/bash

if [ $EUID == 0 ] ; then
    echo "You are root! Please, run me as a normal user."
    exit 1
fi

# WD=$(dirname "$(realpath "$0")")
# SITE_DATA="$WD/site"

docker build --tag luca/jekyll_dev .

