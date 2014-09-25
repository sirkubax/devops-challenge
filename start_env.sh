#!/bin/bash

source .env/bin/activate
./allegro-devop.py > /dev/null 2>&1 &
redis-2.8.17/src/redis-server > /dev/null 2>&1 &

exit 0
