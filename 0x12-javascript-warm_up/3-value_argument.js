#!/usr/bin/node
// prints the first argument passed to it
//
const arg0 = process.argv[2];
if (arg0) {
  console.log(arg0);
} else {
  console.log('No argument');
}
