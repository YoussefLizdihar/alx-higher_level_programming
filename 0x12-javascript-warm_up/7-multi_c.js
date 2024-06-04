#!/usr/bin/node

const arg = process.argv[2];
let i = 0;

while (i < arg) {
  if (isNaN(arg)) {
    console.log('Missing number of occurrences');
  } else {
    console.log('C is fun');
  }
  i++;
}
