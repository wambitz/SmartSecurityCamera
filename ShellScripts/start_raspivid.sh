#!/bin/bash

if pgrep mjpg_streamer > /dev/null
then
    echo "mjpg_streamer already running"
else
    raspivid -t 0 -w 960 -h 540 -fps 25 -b 500000 -vf -o - | ffmpeg -i - -vcodec copy -an -f flv -metadata streamName=myStream tcp://0.0.0.0:6666 > /dev/null 2>&1&
    echo "mjpg_streamer started"
fi

