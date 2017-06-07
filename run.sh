#!/bin/bash
echo 'Export environment varibles...'
export DEV_DATABASE_URL=mysql://root:tribes@121.42.244.187:3382/tribes
export SCRIPT_FOLDER=${PWD}/tribes/script/
export FLASK_APP=${PWD}/tribes/tribes.py

cd tribes/
gunicorn -w 2 -b 0.0.0.0:5001 tribes:app