#!/usr/bin/node

const args = process.argv;
const num1 = Number(args[2]);
const num2 = Number(args[3]);

function add (a, b) {
  return a + b;
}

console.log(add(num1, num2));