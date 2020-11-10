var chakram = require('chakram'),
    expect = chakram.expect;

hostname = 'practice_flask_with_ci_backend-api_1'
hostname_header = ''
port = '8080'
host = 'http://' + hostname + ':' + port

describe("First Page", function() {
    it("should response 200 when get landing page", function () {
        return chakram.get(host + '/')
        .then(function (response) {
           expect(response).to.have.status(200);
        });
    });
});

describe("Backend API basic", function() {
    it("should response 200 when get versoin api", function () {
        return chakram.get(host + '/version')
        .then(function (response) {
           expect(response).to.have.status(200);
        });
    });

    it("should response 200 when get health api", function () {
        return chakram.get(host + '/health')
        .then(function (response) {
           expect(response).to.have.status(200);
           expect(response.body).to.contain('ok');
        });
    });
});
