'use strict';

const test = require('tape');
const isAnagram = require('./04-anagram');

test('check if two words are anagrams', function(t) {
  t.ok(isAnagram('dog', 'god'));
  t.end();
});

test('test invalid inputs', function(t) {
  t.throws(isAnagram.bind(null, [1, 'kutya']));
  t.end();
});