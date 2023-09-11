#!/usr/bin/node
const argLen = process.argv.length;
const myVar = 'Argument found';
const myVar2 = 'Arguments found';
const myVar3 = 'No argument';

if (argLen === 2) {
  console.log(myVar3);
} else if (argLen === 3) {
  console.log(myVar);
} else {
  console.log(myVar2);
}
