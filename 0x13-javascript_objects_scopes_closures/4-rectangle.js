#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++)
        x += 'x';
      if (i < this.height - 1)
        x += '\n';
    }
    console.log(x);
  }

  rotate () {
    this.width = this.height ^ this.width;
    this.height = this.width ^ this.height;
    this.width = this.width ^ this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  };
