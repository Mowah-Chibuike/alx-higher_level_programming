#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data.js').dict;
const values = Object.values(dict);
const sorted = {};
const keys = Object.keys(dict);

for (let i = 0; i < values.length; i++) {
  const arr = [];
  for (let j = 0; j < keys.length; j++) {
    if (dict[keys[j]] === values[i]) {
      arr.push(`${keys[j]}`);
    }
  }
  sorted[`${values[i]}`] = arr;
}

console.log(sorted);
