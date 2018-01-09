'use strict';

let shop_items = ['Cupcake', 2, 'Brownie', false]

// Accidentally we added '2' and 'false' to the array. 
// Your task is to change from '2' to 'Croissant' and change from 'false' to 'Ice cream'
// No, don't just remove the items :)

shop_items.map(function(item, index) {
  if (item === 2) {
    shop_items[index] = 'Croissant';
  } else if (item === false) {
    shop_items[index] = 'Ice cream';
  }
})

console.log(shop_items);
