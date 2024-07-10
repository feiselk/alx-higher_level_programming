#!/usr/bin/node
const OO = parseInt(process.argv[2]);
if (Number.isNaN(OO)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < OO; i++) {
    let M = '';
    for (let j = 0; j < OO; j++) {
      M += 'X';
    }
    console.log(M);
  }
}
