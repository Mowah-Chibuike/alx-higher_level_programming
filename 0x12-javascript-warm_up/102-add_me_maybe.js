#!/usr/bin/node
// exports a function that increments and calls a function.

exports.addMeMaybe = (num, func) => {
  func(++num);
};
