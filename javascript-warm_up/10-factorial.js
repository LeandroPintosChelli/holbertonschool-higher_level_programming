#!/usr/bin/node
// Script that computes and prints a factorial.

const arg = parseInt(process.argv[2]);
function factorial (arg) {
  if (isNaN(arg) || arg === 0) {
    return (1);
  }
  return (arg * factorial(arg - 1));
}
console.log(factorial(arg));
