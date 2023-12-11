#!/usr/bin/node
// prints message based on the number of arguments passed to the script
const { argv } = require('node:process');

const arrayLength = argv.length;
if (arrayLength > 3) {
  console.log('Arguments found');
} else if (arrayLength === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
