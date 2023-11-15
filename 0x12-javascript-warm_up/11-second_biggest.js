#!/usr/bin/node

const { argv } = require('process');
let largest = 0;
let second = 0;
let temp = 0;
if (argv.length >= 4) {
  argv.slice(2).forEach(el => {
    temp = Number(el);
    if (temp > largest) {
      second = largest;
      largest = temp;
    } else if (temp > second) {
      second = temp;
    }
  });
}
console.log(second);
