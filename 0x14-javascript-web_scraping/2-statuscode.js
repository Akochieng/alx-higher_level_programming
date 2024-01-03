#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = argv[2];
try {
  request
    .get(url)
    .on('response', (response) => {
      console.log('code: ' + response.statusCode);
    })
    .on('error', (error) => {
      console.log(error);
    });
} catch (e) {
  console.log(e);
}
