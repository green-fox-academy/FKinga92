// Write the image's url to the console.
//       Replace the image with a picture of your favorite animal.
//       Make the link point to the Green Fox Academy website.
//       Disable the second button.
//       Replace its text with 'Don't click me!'.

let image = document.querySelector('img');
console.log(image.getAttribute('src'));

image.setAttribute('src', 'https://goo.gl/arX8yw');

let link = document.querySelector('a');
link.setAttribute('href', 'https://www.greenfoxacademy.com/');

let secondButton = document.querySelector('.this-one');
secondButton.disabled = true;

secondButton.textContent = 'Don\'t click me!';
