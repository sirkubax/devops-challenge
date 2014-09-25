#!/bin/bash

killall redis-server
ALLEGROPY=`ps aux |grep allegro-devop.py |grep -v grep|awk -F" " '{print $2}'`
kill -9 $ALLEGROPY

exit 0
