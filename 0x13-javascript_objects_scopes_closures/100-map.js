#!/usr/bin/node

const initial = require('./100-data').list;
const newList = initial.map((item, index) => item * index);

console.log(initial);
console.log(newList);
