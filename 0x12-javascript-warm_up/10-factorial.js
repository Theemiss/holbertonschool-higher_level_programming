#!/usr/bin/node

function factorialize (num) {
  let MyRes = 1;
  for (let i = 1; i <= num; i++) {
    MyRes *= i;
  }
  return (MyRes);
}
console.log(factorialize(parseInt(process.argv[2])));
