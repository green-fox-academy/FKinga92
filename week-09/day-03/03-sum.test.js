'use strict';

// Follow these steps:
//   Add a new test case
//   Instantiate your class
//   create a list of integers
//   use the t.equal to test the result of the created sum method
// Run it
// Create different tests where you
// test your method with an empyt list
//   with a list with one element in it
//   with multiple elements in it
//   with a null
//   with a string
// Run them
// Fix your code if needed

const test = require('tape');
const mathClass = require('./03-sum');

test('get sum of elements of a list of integes', function(t) {
  let myClass = new mathClass();

  t.equal(myClass.sum([1, 2, 3]), 6);
  t.equal(myClass.sum([]), 0);
  t.equal(myClass.sum([3]), 3);
  t.equal(myClass.sum([3, 9, 12, 2]), 26);
  t.end();
});

test('get sum of invalid inputs', function(t) {
  let myClass2 = new mathClass();

  t.throws(myClass2.sum.bind(null, null));
  t.throws(myClass2.sum.bind(null, 'alma'));
  t.end();
});