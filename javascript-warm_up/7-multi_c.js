#!/usr/bin/node
// Script that prints x times “C is fun”

const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = num; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
