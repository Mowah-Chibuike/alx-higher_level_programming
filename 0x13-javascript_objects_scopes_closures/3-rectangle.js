#!/usr/bin/node
// contains  a class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 1 && h > 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
