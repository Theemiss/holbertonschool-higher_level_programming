#!/usr/bin/node
const fs = require('fs');
const A = process.argv[2];
const B = process.argv[3];
const C = process.argv[4];
const tA = fs.readFileSync(A, 'utf8');
const tB = fs.readFileSync(B, 'utf-8');
fs.writeFileSync(C, tA + tB);
