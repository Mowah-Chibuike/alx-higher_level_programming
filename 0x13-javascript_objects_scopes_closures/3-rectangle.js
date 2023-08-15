#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!isNaN(Number(w)) && !isNaN(Number(h)) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let strip = '';
    for (let i = 0; i < (this.width ? this.width : 0); i++) {
      strip += 'X';
    }
    for (let i = 0; i < (this.height ? this.height : 0); i++) {
      console.log(strip);
    }
  }
};
