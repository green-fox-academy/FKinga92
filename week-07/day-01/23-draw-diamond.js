'use strict';

let lineCount = 7;

// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is


let x = Math.floor(lineCount / 2);

for (let i = 0; i < x + 1; i++) {
    console.log(' '.repeat(x - i) + '*'.repeat(2 * i + 1) + ' '.repeat(x - i));
}

for (let i = x - 1; i >= 0; i--) {
    console.log(' '.repeat(x - i) + '*'.repeat(2 * i + 1) + ' '.repeat(x - i));
}
