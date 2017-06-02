set DEV_DATABASE_URL=mysql://root:tribes@121.42.244.187:3382/tribes
set FLASK_APP=%cd%\tribes\tribes.py
%cd%\venv\Scripts\flask run -h 127.0.0.1 -p 5001