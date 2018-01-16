'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds


function printFruit(fruit) {
  return function () {
    console.log(fruit);
  };
}

setTimeout(printFruit('grapes'), 5000);
setTimeout(printFruit('melon'), 3000);
setTimeout(printFruit('pear'), 1000);
printFruit('apple')();
