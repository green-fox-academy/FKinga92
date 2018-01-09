'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

let girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
let boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
let order = [];

girls.forEach(function(item, index) {
  order.push(item, boys[index]);
})
console.log(order);
