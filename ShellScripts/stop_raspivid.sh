#!/bin/bash

echo stopping...
if pgrep raspivid
then
    kill $(pgrep raspivid) > /dev/null 2>&1
    echo "raspivid stopped"
else
    echo "raspivid not running"
fi

