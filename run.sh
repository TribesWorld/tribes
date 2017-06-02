export DEV_DATABASE_URL=mysql://root:tribes@121.42.244.187:3382/tribes
export FLASK_APP=${PWD}/tribes/tribes.py
venv/bin/flask run -h 127.0.0.1 -p 5001