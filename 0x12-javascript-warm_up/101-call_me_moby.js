#!/usr/bin/node
/* Function that executes 'number of times' a function */
exports.callMeMoby = function (repeat, theFunction) {
  for (let i = 0; i < repeat; i++) {
    theFunction();
  }
};
