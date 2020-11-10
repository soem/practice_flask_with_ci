var chakram = require('chakram'),
    expect = chakram.expect;
const fs = require('fs');

hostname = 'practice_flask_with_ci_backend-api_1'
hostname_header = ''
port = '8080'
host = 'http://' + hostname + ':' + port

let user_info_1 = JSON.parse(fs.readFileSync('test/user_info/user_info_1.json'));
let user_info_2 = JSON.parse(fs.readFileSync('test/user_info/user_info_2.json'));
let user_info_get = JSON.parse(fs.readFileSync('test/user_info/user_info_2.json'));
let user_info_delete = JSON.parse(fs.readFileSync('test/user_info/user_info_2.json'));

describe("Backend API - User", function () {
    xit("should response 200 when POST to user create api", function () {
        return chakram.post(host + '/api/user/v1/create', JSON.stringify(user_info_1), {
            headers: {
                'content-type': 'application/json'
            }
        })
            .then(function (response) {
                expect(response).to.have.status(200);

                return chakram.get(host + '/api/user/v1/get_profile')
                    .then(function (get_response) {
                        expect(get_response).to.have.status(200);
                        expect(get_response).to.comprise.of.json(user_info_1);
                    });
            });
    });

    xit("should response 200 when GET to user get_profile api", function () {
        return chakram.get(host + '/api/user/v1/get_profile')
            .then(function (response) {
                expect(response).to.have.status(200);
                expect(response).to.comprise.of.json(user_info_get);
            });
    });

    xit("should response 200 when PUT to user force_update api", function () {
        return chakram.put(host + '/api/user/v1/force_update', JSON.stringify(user_info_2), {
            headers: {
                'content-type': 'application/json'
            }
        })
            .then(function (response) {
                expect(response).to.have.status(200);

                return chakram.get(host + '/api/user/v1/get_profile')
                    .then(function (get_response) {
                        expect(get_response).to.have.status(200);
                        // expect(get_response).to.comprise.of.json(user_info_2);
                    });
            });
    });

    xit("should response 200 when DELETE to user delete api", function () {
        return chakram.delete(host + '/api/user/v1/delete', '')
            .then(function (response) {
                expect(response).to.have.status(200);
            });
    });
});
