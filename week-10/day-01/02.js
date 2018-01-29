'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(length, width) {
  this.length = length;
  this.width = width;
}

Rectangle.prototype.getArea = function () {
  return this.length * this.width;
};

Rectangle.prototype.getCircumference = function () {
  return 2 * (this.length + this.width);
};

const rectangle1 = new Rectangle(10, 5);
console.log(rectangle1.getArea());
console.log(rectangle1.getCircumference());
const rectangle2 = new Rectangle(7, 20);
console.log(rectangle2.getArea());
console.log(rectangle2.getCircumference());
