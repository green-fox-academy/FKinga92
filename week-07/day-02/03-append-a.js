'use strict';
// - Create a variable named `am` and assign the value `kuty` to it
// - Write a function called `appendA` that gets a string as an input
//   and appends an 'a' character to its end
// - Print the result of `appendA(am)` to the console

let am = 'kuty';

function appendA(stringToAppend) {
  return (typeof stringToAppend === 'string') ? stringToAppend + 'a' : stringToAppend;
}

console.log(appendA(am));
