#!/usr/bin/node
const myVar = 'C is fun';
const arg1 = parseInt(process.argv[2]);

if (isNaN(arg1)) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < arg1; n++) {
    console.log(myVar);
  }
}
