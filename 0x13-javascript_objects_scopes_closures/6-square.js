#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
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
