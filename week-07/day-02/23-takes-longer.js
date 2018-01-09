'use strict';
// When saving this quote a disk error has occured. Please fix it.
// Add 'always takes longer than' to between the words 'It' and 'you'

let quote = 'Hofstadter\'s Law: It you expect, even when you take into account Hofstadter\'s Law.'
let index = quote.indexOf('It') + 3;
quote = quote.substr(0, index) + 'always takes longer than' + quote.substr(index - 1);

console.log(quote);