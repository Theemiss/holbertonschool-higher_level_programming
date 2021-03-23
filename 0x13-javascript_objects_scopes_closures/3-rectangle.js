#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    let A = '';
    for (let i = 0; i < this.width; i++) {
      A += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(A);
    }
  }
};
