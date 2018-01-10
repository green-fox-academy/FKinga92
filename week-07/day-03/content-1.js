// You can work in the html or in a separate js file. Like:
//     1. Alert the content of the heading.
//     2. Write the content of the first paragraph to the console.
//     3. Alert the content of the second paragraph.
//     4. Replace the heading's content with 'New content'.
//     5. Replace the last paragraph's content with the first paragraph's content.

let heading = document.querySelector('h1');
alert(heading.textContent);

let firstParagraph = document.querySelector('p');
console.log(firstParagraph.textContent);

let secondParagraph = document.querySelector('.other');
alert(secondParagraph.textContent);

heading.textContent = 'New content';

let lastParagraph = document.querySelector('.result');
lastParagraph.textContent = firstParagraph.textContent;
