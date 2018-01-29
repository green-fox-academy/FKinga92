'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(sound) {
  this.sound = sound;
}

Animal.prototype.say = function () {
  console.log(this.sound);
};

const cat = new Animal('meow');
cat.say();

const dog = new Animal('woof');
dog.say();
