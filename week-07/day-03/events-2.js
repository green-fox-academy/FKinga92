// On the click of the button,
//    Count the items in the list
//    And display the result in the result element.

function countItems() {
  let items = document.querySelectorAll('li');
  document.querySelector('.result').textContent = 'There are ' + items.length + ' items in the list.'
}

document.querySelector('button').addEventListener('click', countItems);
