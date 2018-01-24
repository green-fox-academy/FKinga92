'use strict';

// Create a sum method in your class which has a list of integers as parameter
// It should return the sum of the elements in the list


class Math {

  sum(integersToSum) {
    let sum = 0;
    if (Array.isArray(integersToSum) === false) {
      throw new Error('The parameter should not be null.');
    }
    integersToSum.forEach(function(integer) {
      sum += integer;
    });

    if (typeof sum !== 'number') {
      throw new Error('The parameter is not a list of integers.');
    }
    return sum;
  }
}

module.exports = Math;
