#!/bin/bash

source .env/bin/activate
./allegro-devop.py > /dev/null 2>&1 &
redis-server > /dev/null 2>&1 &

exit 0
