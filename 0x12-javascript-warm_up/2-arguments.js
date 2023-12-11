#!/usr/bin/node
// prints message based on the number of arguments passed to the script
const arrayLength = process.argv.length;
if (arrayLength > 3) {
  console.log('Arguments found');
} else if (arrayLength < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
