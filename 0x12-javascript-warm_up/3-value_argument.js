#!/usr/bin/nodejs

const { argv } = require('process');
if (argv[2] !== undefined) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
