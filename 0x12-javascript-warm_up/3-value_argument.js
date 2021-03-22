#!/usr/bin/node
let x = 0;
process.argv.forEach((val, index) => {
  x++;
  if (index === 2) {
    console.log(`${val}`);
  }
});
if (x <= 2) {
  console.log('No argument');
}
