#!/usr/bin/node

const { argv, exit } = require('process');
const request = require('request');
let data = '';
let text = '';
if (!argv[2]) {
  console.log(`Usage: ${argv[1]} episode`);
  exit();
}
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
try {
  request
    .get(url)
    .on('error', (error) => {
      console.log(error);
    })
    .on('response', (response) => {
      response
        .setEncoding('utf-8')
        .on('data', (chunk) => {
          data += chunk;
        })
        .on('end', () => {
          text = JSON.parse(data);
          console.log(text.title);
        });
    });
} catch (e) {
  console.log(e);
}
