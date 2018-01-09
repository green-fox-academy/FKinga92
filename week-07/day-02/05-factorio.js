'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number) {
  let factorial = 1;
  for (let i = 1; i <= number; i++) {
    factorial *= i;
  }
  return factorial;
}
