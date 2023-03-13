#!/usr/bin/node

const args = process.argv;
let list = [];

if (args.length < 4) {
  console.log(0);
} else {
  let length = 0;
  for (let i = 2; i < args.length; i++) {
    list = list.concat(Number(args[i]));
    length++;
  }
  list.sort();
  console.log(list[length - 2]);
}
