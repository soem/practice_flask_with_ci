var chakram = require('chakram'),
    expect = chakram.expect;
const fs = require('fs');

hostname = 'practice_flask_with_ci_backend-api_1'
hostname_header = ''
port = '8080'
host = 'http://' + hostname + ':' + port

let user_info_1 = JSON.parse(fs.readFileSync('test/user_info/user_info_1.json'));
let user_info_2 = JSON.parse(fs.readFileSync('test/user_info/user_info_2.json'));

describe("Backend API - User Normal Flow", function () {
    it("should finish flow when run with create, get, update, delete apis", function () {
        return chakram.post(host + '/api/user/v1/create', user_info_1, {
            headers: {
                'content-type': 'application/json'
            }
        })
        .then(function (create_response) {
            expect(create_response).to.have.status(201);

            return chakram.get(host + '/api/user/v1/get_profile?name=' + user_info_1['name']);
	})
        .then(function (get_response) {
            expect(get_response).to.have.status(200);
            expect(get_response).to.comprise.of.json(user_info_1);

            return chakram.put(host + '/api/user/v1/force_update?name=' + user_info_1['name'], user_info_2, {
                headers: {
                    'content-type': 'application/json'
                }
            });
        })
        .then(function (update_response) {
            expect(update_response).to.have.status(201);

            return chakram.get(host + '/api/user/v1/get_profile?name=' + user_info_2['name']);
        })
        .then(function (get_response) {
            expect(get_response).to.have.status(200);
            expect(get_response).to.comprise.of.json(user_info_2);

            return chakram.delete(host + '/api/user/v1/delete?name=' + user_info_2['name']);
        })
        .then(function (delete_response) {
            expect(delete_response).to.have.status(202);

            return chakram.get(host + '/api/user/v1/get_profile?name=' + user_info_2['name']);
        })
        .then(function (get_response) {
            expect(get_response).to.have.status(404);
        });
    });
});
