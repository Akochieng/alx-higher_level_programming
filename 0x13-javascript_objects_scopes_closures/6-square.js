#!/usr/bin/node

const Square = require('./5-square');
class Square extends Square {
  charPrint(c) {
    let str = '';
    if (c === undefined)
      c = 'x';
    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++)
        str += c;
      if (h < this.height - 1)
        str += '\n';
    }
    console.log(str);
  }
}

