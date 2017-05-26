from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


engine = db.create_engine('mysql://root:tribes@121.42.244.187:3382/tribes')

with engine.connect() as conn:
    result = conn.execute("insert into t_user (name) values ('')")
    print result
