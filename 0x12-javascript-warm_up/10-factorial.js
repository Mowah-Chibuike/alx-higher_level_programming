#!/usr/bin/node
// computes and prints a factorial

function factorial (x) {
  if (x) {
    return (x * factorial(x - 1));
  }
  return (1);
}

const num = Number(process.argv[2]);
console.log(factorial(num));
