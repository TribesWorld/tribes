#!/bin/bash

cd tribes/
gunicorn -w 2 -b 0.0.0.0:5000 tribes:app