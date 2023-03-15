#!/usr/bin/node

const args = process.argv;
const list = [];

console.log(args);
function compareFunc (a, b) {
  if (a < b) {
    return -1;
  } else if (a > b) {
    return 1;
  }
  return 1;
}

if (args.length < 4) {
  console.log(0);
} else {
  let length = 0;
  for (let i = 2; i < args.length; i++) {
    list.push(Number(args[i]));
    length++;
  }
  list.sort(compareFunc);
  console.log(list);
  console.log(list[length - 2]);
}
