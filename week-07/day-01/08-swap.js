'use strict';

// Swap the values of these variables
let a = 123;
let b = 526;

a += b;
b = a - b;
a = a - b;

console.log(a);
console.log(b);
