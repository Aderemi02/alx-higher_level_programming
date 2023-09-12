#!/usr/bin/node

exports.esrever = function (list) {
  const newSet = [];
  for (let n = (list.length - 1); n >= 0; n--) {
    newSet.push(list[n]);
  }
  return newSet;
};
