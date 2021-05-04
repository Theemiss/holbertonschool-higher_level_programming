#!/usr/bin/node

const fs = require('fs');
const FileName = process.argv[2];
const FileContent = process.argv[3];

fs.writeFile(FileName, FileContent, function (err) {
  if (err) {
    console.log(err);
  }
});
