#!/usr/bin/node

function add (a, b) {
  const c = a + b;
  return c;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

const ans = add(arg1, arg2);
console.log(ans);
