#!/bin/sh

ARG="$@"

cd app

case "$ARG" in
    start)
        uvicorn --log-level ${LOG_LEVEL:-info} --host ${HOST:-0.0.0.0} --port ${PORT:-80} app.main:app
    ;;
    dev)
        uvicorn --log-level ${LOG_LEVEL:-info} --host ${HOST:-0.0.0.0} --port ${PORT:-80} app.main:app --reload
    ;;
    test)
        echo "Starting Test"
        uvicorn --log-level ${LOG_LEVEL:-info} --host ${HOST:-0.0.0.0} --port ${PORT:-80} app.main:app --reload &
        echo "Server started"
        pytest -v --setup-show app/tests
    ;;
    *)
        $ARG
    ;;
esac