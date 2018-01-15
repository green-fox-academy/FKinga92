// Create an Animal constructor function
  // Every animal has a hunger property, which is a number
  // Every animal has a thirst property, which is a number
  // When creating a new animal object these properties are created with the default 5 value
  // Every animal can eat() which decreases their hunger by one
  // Every animal can drink() which decreases their thirst by one
  // Every animal can play() which increases both by one
// Create a Farm constructor function
  // The farm has slots which defines the number of free places for animals
  // The farm has list of Animals
  // The farm can breed() which creates a new animal if there's place for it
  // The farm can slaughter() which removes the least hungry animal
  // The farm can print reports about their current state:
    // The farm has 11 living animals we are bankrupt
  // The farm can progress from day to a new day by calling it's progress() method:
    // All animals should have their methods called randomly with 50% chance
    // The farm should call its breed and slaughter method at the end of each day
    // The farm should print report at the end of each day
      // Print the number of sheeps
      // Print "bankrupt" if no animals left
      // Print "okay" if the number of animals is above zero and under the slot number
      // Print "full" if the number of animals are at the maximum allowed

class Animal {
  
  constructor() {
    this.hunger = 5;
    this.thirst = 5;
  }

  eat() {
    this.hunger--;
  }

  drink() {
    this.thirst--;
  }

  play() {
    this.hunger++;
    this.thirst++;
  }
}

class Farm {

  constructor(slot) {
  this.numberOfFreeSlots = slot;
  this.animals = [];
  this.maxSlot = slot;
  }

  fillFarm() {
    for (let i = this.numberOfFreeSlots; i > 0; i--) {
      this.animals.push(new Animal());
      this.numberOfFreeSlots--;
    };
  }

  breed() {
    if (this.numberOfFreeSlots > 0) {
      this.animals.push(new Animal());
      this.numberOfFreeSlots--;
    };
  }

  slaughter() {
    if (this.animals.length === 0) {
      return;
    }

    let hunger = this.animals[0].hunger;
    let indexOfLeastHungryAnimal = 0;
    this.animals.forEach(function(item, index) {
      if (item.hunger < hunger) {
        hunger = item.hunger;
        indexOfLeastHungryAnimal = index;
      }
    });
    this.animals.splice(indexOfLeastHungryAnimal, 1);
    this.numberOfFreeSlots++;
  }

  getStatOfFarm() {
    if (this.animals.length === 0) {
      return 'bankrupt';
    }
    else if (0 < this.animals.length < this.maxSlot) {
      return 'okay';
    }
    else if (this.numberOfFreeSlots === 0) {
      return 'full';
    }
  }


  printReport() {
    let stateOfFarm = this.getStatOfFarm();
    console.log('The farm has ' + this.animals.length + ' living animals, we are ' + stateOfFarm + '.');
  }

  progress() {
    this.animals.forEach(function(item) {
      let methodCallChance = Math.floor(Math.random() * 3);
      if (methodCallChance === 0) {
        item.eat();
      } else if (methodCallChance === 1) {
        item.drink();
      } else {
        item.play();
      }
    });
  
  this.breed();
  this.slaughter();
  this.printReport();
  }
}

const SheepFarm = new Farm(20);
SheepFarm.fillFarm();
console.log(SheepFarm.animals); // Should log 20 Animal objects
SheepFarm.progress();
