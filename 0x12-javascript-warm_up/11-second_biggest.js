#!/usr/bin/node

const list = process.argv.slice(2);
const num = list.map(arg => parseInt(arg));

if (num.length < 2) {
  console.log('0');
} else {
  const arrNum = num.sort((a, b) => b - a);
  console.log(arrNum[1]);
}
