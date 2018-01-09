'use strict';
// Add 'My todo:' to the beginning of the todoText
// Add ' - Download games' to the end of the todoText
// Add ' - Diablo' to the end of the todoText but with indention

// Expected outpt:

// My todo:
//  - Buy milk
//  - Download games
//      - Diablo

let todoText = ' - Buy milk\n';
let indention = '    '
todoText = 'My todo:\n' + todoText + ' - Download games\n' + indention + ' - Diablo';
console.log(todoText);
