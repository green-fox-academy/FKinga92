// Write a function, that takes two strings and returns a boolean value
// based on if the two strings are Anagramms or not.
// Create a test for that.

'use strict';

function getLetters(str) {
  return str.replace(/ /g, '').toLowerCase().split('').sort().join('');
}

let isAnagram = function(str1, str2) {
  if (typeof str1 !== 'string' || typeof str2 !== 'string') {
    throw new Error('The parameters should be strings.')
  }

  return getLetters(str1) === getLetters(str2);
};

module.exports = isAnagram;
