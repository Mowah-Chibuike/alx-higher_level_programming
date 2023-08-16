#!/usr/bin/node

const fs = require('fs');
const readA = process.argv[2];
const readB = process.argv[3];
const write = process.argv[4];

fs.readFile(readA, (err, data) => {
  if (err) {
    throw err;
  }
  const text = data.toString();
  fs.writeFile(write, text, () => {});
});

fs.readFile(readB, (err, data) => {
  if (err) {
    throw err;
  }
  const text = data.toString();
  fs.appendFile(write, text, () => {});
});
