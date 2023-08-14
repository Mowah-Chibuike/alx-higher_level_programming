#!/usr/bin/node
// prints a message depending of the number of arguments passed
const length = process.argv.length;

if (length < 3) {
  console.log('No argument');
} else if (length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
