#!/bin/bash
echo 'Export environment varibles...'
export DEV_DATABASE_URL=mysql://root:tribes@121.42.244.187:3382/tribes
export SCRIPT_FOLDER=${PWD}/tribes/script/

cd tribes/
gunicorn -w 1 -b 0.0.0.0:5001 tribes:tribes