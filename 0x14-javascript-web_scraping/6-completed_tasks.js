#!/usr/bin/node

const request = require('request');
const { argv, exit } = require('process');

if (argv.length !== 3) {
  console.log(`Usage: ${argv[1]} url`);
  exit();
}
async function queryList (url) {
  return (new Promise((resolve, reject) => {
    let data = '';
    let text = '';
    try {
      const req = request.get(url);
      req.on('error', (error) => {
        reject(error);
      });
      req.on('response', (response) => {
        response.setEncoding('utf-8');
        response.on('data', (chunk) => {
          data += chunk;
        });
        response.on('end', () => {
          text = JSON.parse(data);
          resolve(text);
        });
      });
    } catch (e) {
      reject(e);
    }
  }));
}
const aurl = argv[2];
const res = {};
try {
  queryList(aurl)
    .then((todos) => {
      todos.forEach((item) => {
        if (!(item.userId in res)) {
          res[`${item.userId}`] = 0;
        }
        if (item.completed === 'true') {
          res[`${item.userId}`] += 1;
        }
      });
      console.log(res);
    });
} catch (e) {
  console.log(e);
  exit();
}
