#!/usr/bin/node

const argvLength = process.argv.length;

if (argvLength <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.map((ele) => Number(ele)).slice(2).sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
}
