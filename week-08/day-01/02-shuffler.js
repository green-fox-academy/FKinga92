// Create an object called shuffler. It should have a pick() method.

// By default it should have 10000 dollars to shuffle.

// Each time you call pick, it will pick either Panama or Cyprus to deposit some money.
// Decrease the amount by 1000 too
// Console.log which object got how much (eg. Panama got 1000)

// The shuffler will pick on of these:

// Panama object, 1% tax
// Cyprus object, 5% tax
// each object has these properties:

// name
// tax
// cash
// and one method called deposit(amount)


const panama = {
  cash: 0,
  name: 'Panama',
  tax: '1%',
  deposit: function(amount) {
    this.cash += amount;
  }
}

const cyprus = {
  cash: 0,
  name: 'Cyprus',
  tax: '5%',
  deposit: function(amount) {
    this.cash += amount;
  }
}

const shuffler = {
  cash: 10000,
  pick: function() {
    this.cash -= 1000;
    let randomPick = Math.floor(Math.random() * 2);
    if (randomPick === 0) {
      panama.cash += 1000;
      console.log("Panama got 1000.")
    }
    else {
      cyprus.cash += 1000;
      console.log("Cyprus got 1000.")
    }
  }
}

shuffler.pick() // prints Panama got 1000
shuffler.pick() // prints Cyprus got 1000
shuffler.pick() // prints Panama got 1000
shuffler.pick() // prints Cyprus got 1000

console.log(panama.cash ) // 2000 
console.log(cyprus.cash ) // 2000 