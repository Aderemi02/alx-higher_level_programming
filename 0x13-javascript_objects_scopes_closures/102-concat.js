#!/usr/bin/node

const fs = require('fs');
let first = process.argv[2];
let second = process.argv[3];
let result = process.argv[4];
let newfileA = fs.readFileSync(first);
let newfileB = fs.readFileSync(second);
fs.writeFileSync(result, newfileA + newfileB);
