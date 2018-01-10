// You can work in the html or in a separate js file. Like:
//     1. store the element that says 'The King' in the 'king' variable.
//     console.log it.
//     2. store the element that contains the text 'The Conceited Man'
//     in the 'conceited' variable.
//     show the result in an 'alert' window.
//     3. store 'The Businessman' and 'The Lamplighter'
//     in the 'businessLamp' variable.
//     console.log each of them.
//     4. store 'The King' and 'The Conceited Man'
//     in the 'conceitedKing' variable.
//     alert them one by one.
//     5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
//     in the 'noBusiness' variable.
//     console.log each of them.
//     6. store 'The Businessman' in the 'allBizniss' variable.
//     show the result in an 'alert' window.
 
let king = document.getElementById('b325');
console.log(king);

let conceited = document.getElementsByClassName('b326')[0];
alert(conceited.innerHTML);

let businessLamp = document.querySelectorAll('.big');
businessLamp.forEach(function(item) {
  console.log(item);
})

let conceitedKing = document.getElementsByClassName('container')[0].querySelectorAll('.asteroid');
conceitedKing.forEach(function(item) {
  alert(item.innerHTML);
})

let noBusiness = document.querySelectorAll('div');
noBusiness.forEach(function(item) {
  console.log(item);
})

let allBizniss = document.getElementsByTagName('p')[0];
alert(allBizniss.innerHTML);
