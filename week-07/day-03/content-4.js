// 1) replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']
// 2) change the <ul> element's background color to 'limegreen'
//   - don't just add a CSS class
//   - use the .style attribute

let newItems = ['apple', 'banana', 'cat', 'dog'];
let listItems = document.querySelectorAll('li');
listItems.forEach(function(item, index) {
  item.textContent = newItems[index];
})

let unorderedList = document.querySelector('ul');
unorderedList.style.backgroundColor = 'limegreen';
