// Remove the king from the list.

let king = document.querySelector('li');
let unorderedList = document.querySelector('ul');
unorderedList.removeChild(king);

// Fill the list based on the following list of objects.
// Only add the asteroids to the list.
// Each list item should have its category as a class and its content as text content. -->

const planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]

planetData.forEach(function(item) {
  if (item.asteroid) {
    let newItem = document.createElement('li');
    newItem.setAttribute('class', item.category);
    newItem.textContent = item.content;
    unorderedList.appendChild(newItem);
  }
})