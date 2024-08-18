#!/bin/bash

if [[ "$@" == *"--clean"* ]]; then
    rm -r venv
fi

if [ ! -d "venv" ]; then
    python3 -m venv venv
    . venv/bin/activate
    pip install -r src/requirements.txt
else
    . venv/bin/activate
fi

if [[ "$@" == *"--debug"* ]]; then
    python3 src/main.py --debug
else
    python src/main.py
fi
