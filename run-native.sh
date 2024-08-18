#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -r src/requirements.txt
python src/main.py
rm -r venv