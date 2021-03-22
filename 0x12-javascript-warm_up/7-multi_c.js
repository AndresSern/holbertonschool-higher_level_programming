#!/usr/bin/node
/* Script that print 'x' times "C is fun" */
const occurrences = parseInt(process.argv[2]);
if (occurrences === undefined || isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
}
