'use strict';

const test = require('tape');
const getMemberOfFibonacci = require('./06-fibonacci');

test('get n-th member of the Fibonacci sequence', function(t) {
  t.equal(getMemberOfFibonacci(3), 2);
  t.equal(getMemberOfFibonacci(4), 3);
  t.equal(getMemberOfFibonacci(8), 21);
  t.end();
});

test('test invalid inputs', function(t) {
  t.throws(getMemberOfFibonacci.bind(null, ['kutya']));
  t.throws(getMemberOfFibonacci.bind(null, null));
  t.throws(getMemberOfFibonacci.bind(null, []));
  t.end();
});