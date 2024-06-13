#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[2], err => {
  if (err) {
    console.err;
    return;
});
