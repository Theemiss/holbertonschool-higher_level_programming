#!/usr/bin/node
const dict = require('./101-data').dict;
const nDict = {};
for (const key in dict) {
  if (nDict[dict[key]] === undefined) {
    nDict[dict[key]] = [];
  }
  nDict[dict[key]].push(key);
}
console.log(nDict);
