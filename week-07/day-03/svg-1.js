// 1) Select the rectangle by the ID: "very_rectangle"
// 2) Change the rectangle's position to x:50, y:50
// 3) Change its fill to tomato

let rectangle = document.querySelector('#very_rectangle');
rectangle.setAttribute('x', '50');
rectangle.setAttribute('y', '50');
rectangle.style.fill = 'tomato';
