#!/usr/bin/node
exports.esrever = function (list) {
  const newAra = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newAra.push(list[i]);
  }
  return newAra;
};
