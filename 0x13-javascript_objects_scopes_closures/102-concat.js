#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 5) {
  console.error('Not enough arguments');
}

const args = process.argv;
const input1 = args[2];
const input2 = args[3];
const output = args[4];
let data = '';

function read (filename) {
  try {
    const data = fs.readFileSync(filename, 'utf8');
    return data;
  } catch (err) {
    console.log(err);
  }
}

function write (filename, content) {
  try {
    fs.writeFileSync(filename, content);
    return 1;
  } catch (err) {
    console.error(err);
  }
}

function append (filename, content) {
  try {
    fs.appendFileSync(filename, content);
    return 1;
  } catch (err) {
    console.error(err);
  }
}

data = read(input1);
if (data) {
  write(output, data);
}

data = read(input2);
if (data) {
  append(output, data);
}
