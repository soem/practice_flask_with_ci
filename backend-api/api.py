import flask
import json

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
    app.run(host='0.0.0.0', port=8080)
