#!/usr/bin/node

function fact (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const arg1 = parseInt(process.argv[2]);
const ans = fact(arg1);
console.log(ans);
