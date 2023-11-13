#!/usr/bin/nodejs

function secondLargest (arr) {
  let largest = 0;
  let second = 0;
  largest = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= largest) {
      second = largest;
      largest = arr[i];
    } else if (arr[i] >= second) {
      second = arr[i];
    }
  }
  return second;
}

const { argv } = require('process');
const arr = [];
if (argv.length <= 4) {
  console.log(0);
} else {
  argv.slice(2).forEach(el => {
    arr.push(Number(el));
  });
  console.log(secondLargest(arr));
}
