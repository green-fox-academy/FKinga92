'use strict';

let fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

let occurancesOfE = fruits.map(function(fruit) {
  if (fruit.match(/e/gi) !== null) {
    return fruit.match(/e/gi).length;
  }
  else {
    return 0;
  }
});
console.log(occurancesOfE);