#!/usr/bin/node
const SquareA = require('./5-square.js');
module.exports = class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let A = '';
      for (let i = 0; i < this.width; i++) {
        A += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(A);
      }
    }
  }
};
