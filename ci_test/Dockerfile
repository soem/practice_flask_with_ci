FROM node:current-alpine3.12

RUN \
    mkdir -p /app

WORKDIR /app

COPY package.json /app

RUN \
    yarn install

COPY test /app/test

CMD ["/app/node_modules/mocha/bin/mocha"]
