#!/usr/bin/node
/*
 * Write a script that writes a stringto a file
*/

const fs = require('fs');
const file = process.argv[2];
const stringWrite = process.argv[3];

fs.writeFile(file, stringWrite, function (err) {
  if (err) {
    console.log(err);
  }
});
