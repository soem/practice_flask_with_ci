#!/usr/bin/env python3

import flask
import json

from table_users import User, CommunicateInformation, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = {
    "name": "Charles",
    "job_title": "SRE",
    "communicate_information": {
        "email": "charles@gmail.com",
        "mobile": "0911111111"
    }
}

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/api/user/v1/create', methods=['POST'])
def create_user():
    return "<h1>Hello Flask!</h1>"

@app.route('/api/user/v1/get_profile', methods=['GET'])
def user_get_profile():
    session = Session()
    session.close()
    return json.dumps(data)

@app.route('/api/user/v1/force_update', methods=['PUT'])
def user_force_update():
    return "<h1>Hello Flask!</h1>"

@app.route('/api/user/v1/delete', methods=['DELETE'])
def user_delete():
    return "<h1>Hello Flask!</h1>"


@app.route('/version', methods=['GET'])
def version():
    return 'dev'

@app.route('/health', methods=['GET'])
def health():
    return 'ok'

if __name__ == '__main__':
    engine = create_engine('postgresql://postgres:postgres@postgres/postgres', echo=True)

    Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    app.run(host='0.0.0.0', port=8080)

