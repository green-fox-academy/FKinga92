// You can work in the html or in a separate js file. Like:
//   fill every paragraph with the last one's content.

let lastParagraph = document.querySelector('.dog');
let paragraphs = document.querySelectorAll('p');
paragraphs.forEach(function(item) {
  item.textContent = lastParagraph.textContent;
})
