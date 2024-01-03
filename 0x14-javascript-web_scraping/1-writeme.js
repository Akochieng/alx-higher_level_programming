#!/usr/bin/node

const { argv } = require('process');
const { writeFile } = require('fs/promises');

async function writeIt (filePath, content) {
  try {
    await writeFile(filePath, content, 'utf-8');
  } catch (e) {
    console.log(e);
  }
}

writeIt(argv[2], argv[3]);
