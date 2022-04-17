#!/bin/bash

HOST=mongo_db

ping -c1 $HOST 1>/dev/null 2>/dev/null
SUCCESS=$?

if [ $SUCCESS -eq 0 ]
then
  echo "$HOST has replied"
else
  echo "$HOST didn't reply"
fi
#EOF