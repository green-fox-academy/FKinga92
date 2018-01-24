'use strict';

const test = require('tape');
const countLetters = require('./05-count-letters');

test('count letters of a word', function(t) {
  t.deepEqual(countLetters('dog'), {d: 1, o: 1, g: 1});
  t.end();
});

test('test invalid inputs', function(t) {
  t.throws(countLetters.bind(null, [356]));
  t.end();
});