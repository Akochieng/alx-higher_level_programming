#!/usr/bin/node

const request = require('request');
const { argv, exit } = require('process');
let count = 0;
function queryIt (aUrl) {
  return (new Promise((resolve, reject) => {
    let data = '';
    let text = '';
    try {
      request
        .get(aUrl)
        .on('error', (error) => {
          reject(error);
        })
        .on('response', (response) => {
          response
            .setEncoding('utf-8')
            .on('data', (chunk) => {
              data += chunk;
            })
            .on('end', () => {
              text = JSON.parse(data);
              resolve(text);
            });
        });
    } catch (e) {
      reject(e);
    }
  }));
}
async function fetchIt (url) {
  try {
    const res = await queryIt(url);
    return (res);
  } catch (e) {
    console.log(e);
    exit();
  }
}
if (!argv[2]) {
  console.log(`Usage: ${argv[1]} api_url`);
  exit();
}
fetchIt(argv[2])
  .then((result) => {
    result.results.forEach(val => {
      for (const item of val.characters) {
        if (item === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count += 1;
          break;
        }
      }
    });
    console.log(count);
  });
