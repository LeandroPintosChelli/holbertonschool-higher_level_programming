#!/usr/bin/node
// Script that prints a square.

const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i += 1) {
    console.log('X'.repeat(size));
  }
}
