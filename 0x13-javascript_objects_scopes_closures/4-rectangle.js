#!/usr/bin/node
// contains  a class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (!isNaN(Number(w)) && !isNaN(Number(h)) && w > 0 && h > 0) {
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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    if (this.width) {
      this.width *= 2;
    }

    if (this.height) {
      this.height *= 2;
    }
  }
};
