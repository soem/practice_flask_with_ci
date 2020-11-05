docker build -t test-nodejs .
docker run -it --rm --network practice_flask_with_token_based_aa_default test-nodejs:latest
