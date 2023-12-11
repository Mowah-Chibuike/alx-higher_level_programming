#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const myNumber = Math.floor(Number(process.argv[2]));
if (myNumber || myNumber === 0) {
  console.log(myNumber);
} else {
  console.log('Not a number');
}
