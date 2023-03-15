#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const occurences = list.filter((item) => item === searchElement);
  return occurences.length;
}
