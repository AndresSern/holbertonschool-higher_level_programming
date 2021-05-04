#!/usr/bin/node
/*
 * Write a script that writes a stringto a file
*/

const fs = require('fs');
const file = process.argv[2];
const string_write = process.argv[3];

fs.writeFile(file, string_write, function (err) {
  if (err) {
    console.log(error);
  }
});
