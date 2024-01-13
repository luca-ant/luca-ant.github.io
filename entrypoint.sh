#!/bin/bash
set -e

if [ -f Gemfile ]; then
    bundle install --retry 5 --jobs 20
fi

exec "$@"