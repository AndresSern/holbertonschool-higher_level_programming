#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments.  */
function numberBigger (myArray) {
  const indexArray = myArray.indexOf(Math.max(...myArray));
  return myArray.splice(indexArray, 1)[0];
}

const length = process.argv.length;
let myArray = process.argv.splice(2, length);
if (length === 2 || length === 3) {
  console.log('0');
} else {
  myArray = myArray.map(item => parseInt(item));
  const temp = numberBigger(myArray);
  let compare = temp;
  while (compare === temp) {
    compare = numberBigger(myArray);
  }
  console.log(compare);
}
