#!/usr/bin/node
// Script that prints My number: <first argument converted in integer>
// If the first argument can be converted to an integer

const argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argument}`);
}
