#!/usr/bin/nodejs

function factorial (x) {
  if (x === 0 || x === 1 || isNaN(x))
    return 1;
  return x * factorial(x - 1);
}

const { argv } = require('process');
console.log(factorial(Number(argv[2])));
