#!/usr/bin/node

const { argv } = require('process');
const size = Number(argv[2]);
let square = '';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < size; a++) {
    for (let b = 0; b < size; b++) {
      square += 'x';
    }
    if (a < size - 1) { square += '\n'; }
  }
}
console.log(square);
