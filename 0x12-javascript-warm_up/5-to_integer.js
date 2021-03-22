#!/usr/bin/node
const MyVar = process.argv[2];
if (isNaN(MyVar) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + MyVar);
}
