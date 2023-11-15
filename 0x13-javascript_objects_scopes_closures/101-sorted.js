#!/usr/bin/node

const dict = require('./101-data.js').dict;
const keys = Object.keys(dict);
const res = {};
keys.forEach(el => {
  if (res[dict[el]] === undefined) {
    res[dict[el]] = [el];
  } else {
    res[dict[el]].push(el);
  }
});
console.log(res);
