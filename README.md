# practic for flask
flask restful service w/ CRUD api


## Start User Service
```bash
docker-compose build
docker-compose up -d
```

## Run test cases
```bash
bash ci_test.sh
```

## API example

### create user
```bash
curl 'http://127.0.0.1:8080/api/user/v1/create' \
    -v -s -X POST \
    -d @ci_test/test/user_info/user_info_1.json \
    -H 'Content-Type: application/json'
```

### update user
```bash
curl 'http://127.0.0.1:8080/api/user/v1/force_update?name=Charles' \
    -v -s -X PUT \
    -d @ci_test/test/user_info/user_info_2.json \
    -H 'Content-Type: application/json'
```

### get user
```bash
curl 'http://127.0.0.1:8080/api/user/v1/get_profile?name=Bob' \
    -v -s 
```

### update user
```bash
curl 'http://127.0.0.1:8080/api/user/v1/delete?name=Bob' \
    -v -s -X DELETE
```