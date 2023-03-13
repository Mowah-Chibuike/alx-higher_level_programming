#!/usr/bin/node

const x = Number(process.argv[2]);
let strip = '';

if (x) {
  for (let i = 0; i < x; i++) {
    strip += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(strip);
  }
} else {
  console.log('Missing size');
}
