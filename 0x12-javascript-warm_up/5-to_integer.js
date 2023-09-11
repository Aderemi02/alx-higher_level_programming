#!/usr/bin/node
const arg1 = process.argv[2];
const convInt = parseInt(arg1);

if (isNaN(convInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convInt);
}
