#!/usr/bin/node
let x = 0;
process.argv.forEach((val, index) => {
  x++;
});
if (x <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
