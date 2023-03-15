#!/usr/bin/node

function preLogMe() {
  let printed = 0;
  return (arg) => {
    console.log(`${printed}: ${arg}`);
    printed++;
  }
}

exports.logMe = preLogMe()
