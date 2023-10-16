#!/bin/sh

ARG="$@"


case "$ARG" in
    start)
    echo " THE VALUE ENTERRED FOR ARG IS start"
        uvicorn --log-level ${LOG_LEVEL:-info} --host ${HOST:-0.0.0.0} --port ${PORT:-80} app.main:app
    ;;
    dev)
        echo " THE VALUE ENTERRED FOR ARG IS ${ARG}"
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