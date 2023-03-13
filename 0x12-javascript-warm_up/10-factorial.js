#!/usr/bin/node

const num = Number(process.argv[2]);

function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  }
  return x * factorial(--x);
}

console.log(factorial(num));
