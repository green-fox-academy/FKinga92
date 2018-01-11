'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

let matrixSize = 4;
let matrix = [];

for (let i = matrixSize - 1; i >= 0; i--) {
  let matrixRow = [];
  for (let j = 0; j  < matrixSize; j++) {
    if (j === i) {
      matrixRow.push(1);
    } else {
      matrixRow.push(0);
    }
  }
  matrix.push(matrixRow);
}

matrix.forEach(function(item) {
  console.log(item.join(' '));
})
