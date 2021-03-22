#!/usr/bin/node
/* Script that prints 'My number: <first argument convertd in integer if the
 * first argument can be converted to an integer' */
const stringToNumber = parseInt(process.argv[2]);
if (isNaN(stringToNumber)) console.log('Not a number');
else console.log(`My number: ${stringToNumber}`);
