#!/usr/bin/node
function nextBiggest (arr) {
  let max = 0; let result = 0;

  for (const value of arr) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr];
    } else if (nr < max && nr > result) {
      result = nr;
    }
  }

  return result;
}

console.log(nextBiggest(process.argv));
