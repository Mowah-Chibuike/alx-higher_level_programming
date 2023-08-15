#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!isNaN(Number(w)) && !isNaN(Number(h)) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
