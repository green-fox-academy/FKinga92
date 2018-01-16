// Create a simple HTML document with one button.
// If the user clicks the button 3 times, and 5 seconds is already ellapsed since the page is loaded,
// a text should apper under the button:
// 5 seconds ellapsed and clicked 3 times
// If the user starts clicking before the first 5 seconds, nothing should be printed

'use strict';

let button = document.querySelector('button');
let body = document.querySelector('body');
let counter = 0;

function showText() {
  let paragraph = document.createElement('p');
  paragraph.innerHTML = '5 seconds elapsed and clicked 3 times';
  body.appendChild(paragraph);
}

function countClicks() {
  counter++;

  if (counter === 3) {
    showText();
  }
}

function allowClicks() {
  button.addEventListener('click', countClicks);
}

setTimeout(allowClicks, 5000);



