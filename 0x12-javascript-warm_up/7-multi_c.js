#!/usr/bin/node
const MyVar = process.argv[2];
if (isNaN(MyVar) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < MyVar; i++) {
    console.log('C is fun');
  }
}
