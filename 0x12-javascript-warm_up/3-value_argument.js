#!/usr/bin/node
/* Script that prints the first argument passed to it */
const item = process.argv[2];
if (item === undefined) console.log('No argument');
else console.log(item);
