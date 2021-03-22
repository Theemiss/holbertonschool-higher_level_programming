#!/usr/bin/node
exports.callMeMoby = function (num, theFunction) {
  for (let i = 0; i < num; i++) {
    theFunction();
  }
};
