// Add an item that says 'The Green Fox' to the asteroid list.
//       Add an item that says 'The Lamplighter' to the asteroid list.
//       Add a heading saying 'I can add elements to the DOM!' to the .container.
//       Add an image, any image, to the container.

let unorderedList = document.querySelector('ul');
let greenFox = document.createElement('li');
greenFox.textContent = 'The Green Fox';
unorderedList.appendChild(greenFox);

let lapmlighter = document.createElement('li');
lapmlighter.textContent = 'The Lamplighter';
unorderedList.appendChild(lapmlighter);

let heading = document.createElement('h1');
heading.textContent = 'I can add elements to the DOM!';
document.querySelector('.container').appendChild(heading);

let image = document.createElement('img');
image.setAttribute('src', 'https://goo.gl/cfZT4W');
document.querySelector('.container').appendChild(image);
