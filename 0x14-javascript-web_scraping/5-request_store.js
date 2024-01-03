#!/usr/bin/node

const { argv, exit } = require('process');
const request = require('request');
const { writeFile } = require('fs/promises');

if (argv.length !== 4) {
  console.log(`Usage: ${argv[1]} url filepath`);
  exit();
}
async function fetchContent (url) {
  return (new Promise((resolve, reject) => {
    let data = '';
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
          resolve(data);
        });
      });
    } catch (e) {
      reject(e);
    }
  }));
}

async function writeIt (content, file) {
  try {
    await writeFile(file, content, 'utf-8');
  } catch (e) {
    console.log(e);
    exit();
  }
}

try {
  const url = argv[2];
  const file = argv[3];
  fetchContent(url)
    .then((content) => {
      writeIt(content, file);
    });
} catch (e) {
  console.log(e);
  exit();
}
