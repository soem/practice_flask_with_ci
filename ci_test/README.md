docker build -t test-nodejs .
docker run -it --rm --network practice_flask_with_ci_default test-nodejs:latest
