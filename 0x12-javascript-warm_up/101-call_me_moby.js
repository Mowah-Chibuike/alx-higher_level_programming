#!/usr/bin/node
// contains  a function that executes x times a function.

exports.callMeMoby = (x, func) => {
  for (let i = 0; i < x; i++) {
    func();
  }
};
