#!/usr/bin/node
let Max = 0;
const MyArr = process.argv;
if (MyArr.length === 3) {
  Max = 0;
} else {
  for (let i = 2; i <= MyArr.length; i++) {
    if (parseInt(MyArr[i]) >= Max) {
      Max = MyArr[i];
    }
  }
}

console.log(Max);
