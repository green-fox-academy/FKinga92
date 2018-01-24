'use strict';

// Adds a and b, returns as result
const addNumbers = function(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Invalid value');
  }

  return a + b;
}

// Returns the highest value from the three given params
const maxOfThree = function(a, b, c) {
  if (typeof a !== 'number' || typeof b !== 'number' || typeof c !== 'number') {
    throw new Error('Invalid value');
  }

  return Math.max(a, b, c);
}

//Returns the median value of a list given as param
const median = function(pool) {
  if (pool.filter(item => typeof item !== 'number').length > 0) {
    return 'Invalid value';
  }

  return (pool.length % 2 !== 0)
          ? (pool.sort()[Math.floor(pool.length / 2)])
          : ((pool.sort()[(pool.length / 2)] + pool.sort()[(pool.length / 2) - 1]) / 2);
}

// Returns true if the param is a vovel
const isVovel = function(char) {
  if (char.length !== 1) {
    return 'Please, give me one character';
  }

  return 'aeiouéáőűöüóí'.indexOf(char.toLowerCase()) > -1;
}

// Create a method that translates hungarian into the teve language
const translate = function(hungarian) {
  if (typeof hungarian !== 'string') {
    return 'Invalid value';
  }

  let teve = '';
  hungarian.split('').forEach(function(char) {
    if (isVovel(char)) {
      teve += char + 'v'+ char;
    }
    else {
      teve += char;
    }
  });
  return teve;
}

module.exports = {
  addNumbers: addNumbers,
  maxOfThree: maxOfThree,
  median: median,
  isVovel: isVovel,
  translate: translate
}