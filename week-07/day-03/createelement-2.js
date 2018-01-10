// Remove the Mega juicy candy from the list.
//       Add 16 list items saying 'Empty box' to the list and add an index to it, like:
//       Empty box #1
//       Empty box #2
//       Empty box #3

let megaJuicyCandy = document.querySelector('li');
let unorderedList = document.querySelector('ul');
unorderedList.removeChild(megaJuicyCandy);

for (let i = 1; i <= 16; i++) {
  let newElement = document.createElement('li');
  newElement.textContent = ' Empty box #' + i;
  unorderedList.appendChild(newElement);
}
