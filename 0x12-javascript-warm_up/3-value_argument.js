#!/usr/bin/node
const arg1 = process.argv[2];
const myVar3 = 'No argument';

if (arg1) {
  console.log(arg1);
} else {
  console.log(myVar3);
}
