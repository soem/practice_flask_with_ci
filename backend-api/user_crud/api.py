#!/usr/bin/env python3

import flask
from flask import request, Response
import json

from table_users import User, CommunicateInformation, Base
from sqlalchemy import create_engine, exc
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
    post_data = request.get_json()
    if post_data == None:
        return 'bad'

    name = post_data['name']
    job_title = post_data['job_title']
    new_user = User(name=name, job_title=job_title)

    session = Session()
    try:
        user = session.query(User).filter(User.name==name).first()
        print(user)
        if user != None:
            print(user)
    except exc.SQLAlchemyError:
        user_profile = {}

    finally:
        session.close()

    return '{"msg": "Created."}'

@app.route('/api/user/v1/get_profile', methods=['GET'])
def user_get_profile():
    name = request.args.get('name')
    session = Session()
    try:
        user_profile = session.query(CommunicateInformation).\
                            join(CommunicateInformation.user).\
                            filter(User.name==name).first()
    except exc.SQLAlchemyError as e:
        print(e)
        user_profile = None

    finally:
        session.close()

    if user_profile:
        return json.dumps(user_profile)

    return Response(
        '{"msg": "%s not found!"}' % (name),
        status=404,
        mimetype='application/json'
    )

@app.route('/api/user/v1/force_update', methods=['PUT'])
def user_force_update():
    return "<h1>Hello Flask!</h1>"

@app.route('/api/user/v1/delete', methods=['DELETE'])
def user_delete():
    name = request.args.post('name')
    session = Session()
    try:
        user_profile = session.query(CommunicateInformation).\
                            join(CommunicateInformation.user).\
                            filter(User.name==name).first()

        session.delete(user_profile)
        session.delete(user_profile.User)
        session.commit()
    except exc.SQLAlchemyError as e:
        print(e)
        user_profile = None

    finally:
        session.close()

    if user_profile:
        return json.dumps(user_profile)

    return Response(
        '{"msg": "%s not found!"}' % (name),
        status=404,
        mimetype='application/json'
    )


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

