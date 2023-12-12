#!/usr/bin/node
// imports an array and computes a new array

const list = require('./100-data').list;

console.log(list);
console.log(list.map((i, element) => element * i));
