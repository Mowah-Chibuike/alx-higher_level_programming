#!/usr/bin/node

const x = Number(process.argv[2]);
const strip = '';

if (x) {
  for (let i = 0; i < x; i++) {
    strip.concat('X');
  }
  for (let i = 0; i < x; i++) {
    console.log(strip);
  }
} else {
  console.log('Missing size');
}
