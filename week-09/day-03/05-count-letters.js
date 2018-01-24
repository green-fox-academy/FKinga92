'use strict';
// Write a function, that takes a string as an argument and returns a dictionary
// with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
// Create a test for that.

let countLetters = function(stringToCheck) {
  if (typeof stringToCheck !== 'string') {
    throw new Error(stringToCheck + ' is not a string.');
  }

  let letterCount = {};
  for (let i = 0; i < stringToCheck.length; i++) {
    let letter = stringToCheck[i]
    let regexp = new RegExp(letter, 'gi');
    letterCount[letter] = stringToCheck.match(regexp).length;
  }
  return letterCount;
};

module.exports = countLetters;
