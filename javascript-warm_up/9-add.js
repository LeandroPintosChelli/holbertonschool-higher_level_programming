#!/usr/bin/node
// Script that prints the addition of 2 integers

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (x, z) {
  return (x + z);
}
console.log(add(a, b));
