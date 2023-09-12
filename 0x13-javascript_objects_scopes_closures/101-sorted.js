#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newdict = {};

for (const key in dict) {
  const value = dict[key].toString();
  if (newdict[value]) {
    newdict[value].push(key);
  } else {
    newdict[value] = [key];
  }
}
console.log(newdict);
