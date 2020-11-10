#!/bin/bash


docker-compose -f docker-compose_ci.yaml build
docker-compose -f docker-compose_ci.yaml up -d

docker build -t test-nodejs ci_test
docker run -it --rm --network practice_flask_with_token_based_aa_ci test-nodejs:latest
status=$?

docker-compose -f docker-compose_ci.yaml down
exit $status

