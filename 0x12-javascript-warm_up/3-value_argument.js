#!/usr/bin/node
// Prints the first argument passed to it
const args = process.argv.slice(2);
const firstArgument = args[0] != undefined ? args[0] : 'No argument';

console.log(firstArgument)
