#!/usr/bin/env python3

import flask
from flask import request, Response
import json

from table_users import User, CommunicateInformation, Base
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def check_user_data(user_data):
    data_keys = user_data.keys()
    for key in ['name', 'job_title', 'communicate_information']:
        if key not in data_keys:
            return False

    data_comm_keys = user_data['communicate_information'].keys()
    for key in ['email', 'mobile']:
        if key not in data_comm_keys:
            return False
    
    return True

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
    post_data_str = request.get_json()
    if post_data_str == None:
        return Response(
            '{"msg": "post empty data!"}',
            status=400,
            mimetype='application/json'
        )

    post_data = json.loads(post_data_str)
    if not check_user_data(post_data):
        return Response(
            '{"msg": "post format error!"}',
            status=400,
            mimetype='application/json'
        )

    name = post_data['name']
    job_title = post_data['job_title']
    comm_info = post_data['communicate_information']

    session = Session()
    try:
        new_user = User(name=name, job_title=job_title)
        session.add(new_user)
        session.commit()

        new_user_comm = CommunicateInformation(email=comm_info['email'], mobile=comm_info['mobile'],user_id=new_user.id)
        session.add(new_user_comm)
        session.commit()

        res = Response(
            '{"msg": "creation succeed!!"}',
            status=201,
            mimetype='application/json'
        )

    except exc.SQLAlchemyError:
        session.rollback()
        res = Response(
            '{"msg": "creation failed!!"}',
            status=500,
            mimetype='application/json'
        )

    finally:
        session.close()

    return res

@app.route('/api/user/v1/get_profile', methods=['GET'])
def user_get_profile():
    name = request.args.get('name')
    session = Session()
    try:
        user_data = session.query(User).\
                            join(User.communicate_information).\
                            filter(User.name==name).first()

        if user_data:
            user_profile_res = {
                "name": user_data.name,
                "job_title": user_data.job_title,
                "communicate_information": {
                    "email": user_data.communicate_information.email,
                    "mobile": user_data.communicate_information.mobile
                }
            }

        else:
            user_profile_res = None

    except exc.SQLAlchemyError as e:
        print(e)
        user_profile_res = None

    finally:
        session.close()

    if user_profile_res:
        return Response(
            json.dumps(user_profile_res),
            status=200,
            mimetype='application/json'
        )

    return Response(
        '{"msg": "%s not found!"}' % (name),
        status=404,
        mimetype='application/json'
    )

@app.route('/api/user/v1/force_update', methods=['PUT'])
def user_force_update():
    post_data_str = request.get_json()
    old_name = request.args.get('name')
    if not old_name:
        return Response(
            '{"msg": "name parameter should not be empty!"}',
            status=400,
            mimetype='application/json'
        )

    if post_data_str == None:
        return Response(
            '{"msg": "post empty data!"}',
            status=400,
            mimetype='application/json'
        )

    post_data = json.loads(post_data_str)
    if not check_user_data(post_data):
        return Response(
            '{"msg": post format error!"}',
            status=400,
            mimetype='application/json'
        )

    name = post_data['name']
    job_title = post_data['job_title']
    comm_info = post_data['communicate_information']

    session = Session()
    try:
        user_data = session.query(User).filter(User.name==old_name).first()
        if user_data == None:
            res = Response(
                '{"msg": "%s not found!"}' % (old_name),
                status=404,
                mimetype='application/json'
            )
        else:
            print(user_data.communicate_information)
            session.query(CommunicateInformation).\
                            filter(CommunicateInformation.user_id==user_data.id).\
                            update({'email': comm_info['email'], 'mobile': comm_info['mobile']})
            session.query(User).filter(User.name==old_name).update({'name': name, 'job_title': job_title})
            session.commit()

            res = Response(
                '{"msg": "upsert succeed!!"}',
                status=201,
                mimetype='application/json'
            )

    except exc.SQLAlchemyError as e:
        print(e)
        session.rollback()
        res = Response(
            '{"msg": "upsert failed!!"}',
            status=500,
            mimetype='application/json'
        )

    finally:
        session.close()

    return res

@app.route('/api/user/v1/delete', methods=['DELETE'])
def user_delete():
    name = request.args.get('name')
    session = Session()
    try:
        user_data = session.query(User).\
                            join(User.communicate_information).\
                            filter(User.name==name).first()
        if user_data == None:
            succeed = False

        else:
            session.delete(user_data.communicate_information)
            session.delete(user_data)
            session.commit()
            succeed = True

    except exc.SQLAlchemyError as e:
        print(e)
        succeed = False

    finally:
        session.close()


    if succeed:
        return Response(
            '{"msg": "%s has been deleted!"}' % (name),
            status=202,
            mimetype='application/json'
        )

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
    postgres_db = os.environ['POSTGRES_DB']
    postgres_user = os.environ['POSTGRES_USER']
    postgres_password = os.environ['POSTGRES_PASSWORD']

    postgres_host = os.environ['POSTGRES_HOST']

    engine = create_engine(
                 'postgresql://%s:%s@%s/%s' % (postgres_user, postgres_password, postgres_host, postgres_db),
                 echo=True
             )

    Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    app.run(host='0.0.0.0', port=8080)

