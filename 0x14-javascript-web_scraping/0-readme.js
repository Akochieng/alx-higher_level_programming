#!/usr/bin/node

const { argv } = require('process');
const { readFile } = require('fs/promises');

async function readIt (filePath) {
  try {
    const text = await readFile(filePath, 'utf-8');
    console.log(text);
  } catch (e) {
    console.log(e);
  }
}

readIt(argv[2]);
