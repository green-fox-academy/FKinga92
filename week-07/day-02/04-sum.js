'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(rangeEnd) {
  let sum = 0;
  for (let i = 1; i < rangeEnd; i++) {
    sum += i;
  }
  return sum;
}
