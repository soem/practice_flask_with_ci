var chakram = require('chakram'),
    expect = chakram.expect;

hostname = 'practice_flask_with_token_based_aa_backend-api_1'
hostname_header = ''
port = '8080'
host = 'http://' + hostname + ':' + port

describe("Backend API - User", function() {
    it("should response 200 when POST to user create api", function () {
        return chakram.post(host + '/api/user/v1/create', '')
        .then(function (response) {
           expect(response).to.have.status(200);
        });
    });

    it("should response 200 when GET to user get_profile api", function () {
        return chakram.get(host + '/api/user/v1/get_profile')
        .then(function (response) {
           expect(response).to.have.status(200);
        });
    });

    it("should response 200 when PUT to user force_update api", function () {
        return chakram.put(host + '/api/user/v1/force_update', '')
        .then(function (response) {
           expect(response).to.have.status(200);
        });
    });

    it("should response 200 when DELETE to user delete api", function () {
        return chakram.delete(host + '/api/user/v1/delete', '')
        .then(function (response) {
           expect(response).to.have.status(200);
        });
    });
});
