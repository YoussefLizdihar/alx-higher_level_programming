#!/usr/bin/node

const arg = process.argv[2];
let i = 0;
let j = 0;

while (i < arg) {
  while (j < arg) {
    console.log('X');
    j++;
  }
  j = 0;
  i++;
}
