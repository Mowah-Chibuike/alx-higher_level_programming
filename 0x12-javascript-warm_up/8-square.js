#!/usr/bin/node
// prints a square of size x. Where x is the first argument to the script

const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < size; i++) {
    row += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
