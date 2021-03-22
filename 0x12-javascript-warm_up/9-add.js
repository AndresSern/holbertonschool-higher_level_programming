#!/usr/bin/node
/* Script that prints the addition of 2 integers */
const number1 = parseInt(process.argv[2]);
const number2 = parseInt(process.argv[3]);
function add (a, b) {
  return a + b;
}
console.log(add(number1, number2));
