#!/usr/bin/node
// exports a function that returns the reversed version of a list

exports.esrever = function (list) {
  const reversed = [];
  list.forEach((element) => {
    reversed.unshift(element);
  });
  return reversed;
};
