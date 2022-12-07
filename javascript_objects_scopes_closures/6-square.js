#!/usr/bin/node
// Class Square that defines a square
// and inherits from Square of 5-square.js

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
