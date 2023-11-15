#!/usr/bin/node

const Sq = require('./5-square');
class Square extends Sq {
  constructor (width) {
    super(width, width);
  }

  charPrint = function (c) {
    let str = '';
    if (c === undefined) { c = 'X'; }
    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++) { str += c; }
      if (h < this.height - 1) { str += '\n'; }
    }
    console.log(str);
  };
}
module.exports = Square;
