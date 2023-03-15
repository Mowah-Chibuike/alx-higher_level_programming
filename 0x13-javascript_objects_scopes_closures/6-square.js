#!/usr/bin/node

const parentSquare = require('./5-square.js');

module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (c !== undefined) {
      let strip = '';
      for (let i = 0; i < this.width; i++) {
        strip += c;
      }
      for (let i = 0; i < this.width; i++) {
        console.log(strip);
      }
    } else {
      this.print();
    }
  }
};
