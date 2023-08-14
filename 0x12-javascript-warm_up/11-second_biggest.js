#!/usr/bin/node

const argv_length = process.argv.length;

if (argv_length <= 3)
{
  console.log(0);
} else {
  const numbers = process.argv.slice(2);
  numbers.sort();
  console.log(numbers[numbers.length - 2]);
}
