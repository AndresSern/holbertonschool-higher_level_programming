#!/usr/bin/node
/* Script that prints a square with the letter 'X' */
const occurrences = parseInt(process.argv[2]);

if (occurrences === undefined || isNaN(occurrences)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < occurrences; i++) {
    console.log('X'.repeat(occurrences));
  }
}
