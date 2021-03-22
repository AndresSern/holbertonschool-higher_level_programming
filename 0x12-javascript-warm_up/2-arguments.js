#!/usr/bin/node
/* Script that prints a message depending of the number of arguments passed */
const argvLength = process.argv.length;
if (argvLength === 2) console.log('No argument');
else if (argvLength === 3) console.log('Argument found');
else console.log('Arguments found');
