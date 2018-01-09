'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

let listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16];

function numChecker(arrayToCheck) {
  return (arrayToCheck.indexOf(4) > 0
          && arrayToCheck.indexOf(8) > 0
          && arrayToCheck.indexOf(12) > 0
          && arrayToCheck.indexOf(16) > 0
  );
}

console.log(numChecker(listOfNumbers));
