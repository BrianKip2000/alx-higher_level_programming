#!/usr/bin/node
const a = Math.floor(Number(process.argv[2]));
if (isNaN(a)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    let c = '';
    for (let j = 0; j < a; j++) c += 'X';
    console.log(c);
  }
}
