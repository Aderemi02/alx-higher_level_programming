#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let n = 0; n < list.length; n++) {
    if (searchElement === list[n]) {
      num++;
    }
  }
  return num;
};
