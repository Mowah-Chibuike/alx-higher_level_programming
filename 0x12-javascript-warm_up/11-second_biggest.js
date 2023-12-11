#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const argvLength = process.argv.length;

if (argvLength > 3) {
  const numbers = process.argv.map((ele) => Number(ele)).slice(2).sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
} else {
  console.log(argv[0]);
}
