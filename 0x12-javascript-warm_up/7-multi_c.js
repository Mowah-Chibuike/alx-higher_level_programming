#!/usr/bin/node
// prints x times “C is fun”. Where x is the first argument of the script

const times = Number(process.argv[2]);
if (times) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
