#!/usr/bin/node

exports.esrever = function (list) {
  const newarr = [];
  list.forEach((item) => newarr.unshift(item));
  return (newarr);
};
