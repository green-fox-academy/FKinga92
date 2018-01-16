// Create a simple HTML document with one button.
// If the user clicks the button it should wait 2 seconds and it should show a text under the button:
// 2 seconds ellapsed

let button = document.querySelector('button');
let body = document.querySelector('body');

function showText() {
  let paragraph = document.createElement('p');
  paragraph.innerHTML = '2 seconds ellapsed';
  body.appendChild(paragraph);
}

function delay() {
  setTimeout(showText, 2000);
}

button.addEventListener('click', delay);
