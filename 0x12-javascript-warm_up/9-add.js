#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const { argv } = require('process');
console.log(add(Number(argv[2]), Number(argv[3])));
