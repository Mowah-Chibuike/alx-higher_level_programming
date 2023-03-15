#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).forEach((item) => {
  if (newDict[dict[item]] === undefined) {
    newDict[dict[item]] = [item];
  } else {
    newDict[dict[item]].push(item);
  }
});

console.log(newDict);
