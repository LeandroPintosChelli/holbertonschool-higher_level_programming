#!/usr/bin/node
// Script that reads and prints the content of a file.

const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', function (error, info) {
  if (error) {
    console.log(error);
  } else {
    console.log(info);
  }
});
