#!/usr/bin/node

const length = Number(process.argv[2]);

if (isNaN(length)) {
  console.log('Missing size');
} else {
  let width = '';
  for (let i = 0; i < length; i++) {
    width += 'X';
  }
  for (let i = 0; i < length; i++) {
    console.log(width);
  }
}
