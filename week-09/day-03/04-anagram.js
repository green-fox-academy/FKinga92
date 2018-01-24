// Write a function, that takes two strings and returns a boolean value
// based on if the two strings are Anagramms or not.
// Create a test for that.

'use strict';

let isAnagram = function(str1, str2) {
  if (typeof str1 !== 'string' || typeof str2 !== 'string') {
    throw new Error('The parameters should be strings.')
  }

  return str1.replace(/ /g, '').toLowerCase().split('').sort().join('') === str2.replace(/ /g, '').toLowerCase().split('').sort().join('');
};

module.exports = isAnagram;
