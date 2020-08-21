#!/bin/bash

set -e

if [ -z $LOCUSTFILE_PATH ] || [ -z $TARGET_URL ]; then
  echo "You must set the locust file path (LOCUSTFILE_PATH) and target url (TARGET_URL) to run this image"
  exit 1
fi
if [ -z $PORT ]; then
  export PORT=8089
fi
if [ -z $LOG_LEVEL ]; then
  export LOG_LEVEL=DEBUG
fi

set LOCUST_OPTS=
LOCUST_OPTS+=( -f $LOCUSTFILE_PATH )
LOCUST_OPTS+=( --loglevel $LOG_LEVEL )

case "$MODE" in
  master)
    LOCUST_OPTS+=( --master -H $TARGET_URL -P $PORT )
    ;;
  worker)
    LOCUST_OPTS+=( --worker --master-port $PORT --master-host $TARGET_URL )
    ;;
  *)
    LOCUST_OPTS+=( -H $TARGET_URL -P $PORT )
    ;;
esac

echo "Running locust with ${LOCUST_OPTS[@]}"
locust ${LOCUST_OPTS[@]}
