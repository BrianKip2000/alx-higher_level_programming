#!/usr/bin/node
// Prints the first argument passed to it
const { argv } = require('node:process')

if (argv.length <= 2) {
    console.log('No argument');
} else if (argv.length > 2) {
    console.log(`${argv[2]}`);
}