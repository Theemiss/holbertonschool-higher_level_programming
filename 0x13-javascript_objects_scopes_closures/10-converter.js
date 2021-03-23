#!/usr/bin/node
exports.converter = function (base) {
  function conv (number) {
    return number.toString(base);
  }
  return conv;
};
