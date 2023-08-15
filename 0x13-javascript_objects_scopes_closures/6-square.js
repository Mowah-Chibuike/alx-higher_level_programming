#!/usr/bin/node

const Square0 = require('./5-square');

module.exports = class Square extends Square0 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let strip = '';
    for (let i = 0; i < this.width; i++) {
      strip += c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(strip);
    }
  }
};
