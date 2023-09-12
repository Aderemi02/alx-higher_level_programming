#!/usr/bin/node
const list = require('./100-data.js').list;
const newSet = list.map((curr, ind) => {
  return (curr * ind);
});
console.log(list);
console.log(newSet);
