'use strict';

let lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (let i = lineCount - 1; i >= 0; i--) {
    console.log(' '.repeat(i) + '*'.repeat(2 * lineCount - 1 - 2 * i) + ' '.repeat(i));
}
