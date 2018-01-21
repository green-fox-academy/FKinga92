let section = document.querySelector('section');
let buttons = document.querySelectorAll('button');

class ElevatorModel {

  constructor(maxFloor, maxPeople) {
    this.maxFloor = maxFloor;
    this.maxPeople = maxPeople;
    this.elevatorPosition = 0;
    this.numberOfPeople = 0;
  }

  addPeople() {
    if (this.numberOfPeople < this.maxPeople) {
      this.numberOfPeople++;
    } else {
      console.log('The elevator is full.');
    }
  }

  removePeople() {
    if (this.numberOfPeople > 0) {
      this.numberOfPeople--;
    } else {
      console.log('The elevator is empty.');
    }
  }

  moveUp() {
    if (this.elevatorPosition < this.maxFloor -1) {
      this.elevatorPosition++;
    } else {
      console.log('The elevator is at the top floor.')
    }
  }

  moveDown() {
    if (this.elevatorPosition > 0) {
      this.elevatorPosition--;
    } else {
      console.log('The elevator is at the ground floor.')
    }
  }
}

class ElevatorView {

  constructor(elevator) {
    this.elevator = elevator;
  }

  drawFloors() {
    for (let i = 0; i < this.elevator.maxFloor; i++) {
      let floor = document.createElement('p');
      floor.textContent = this.elevator.numberOfPeople;
      floor.id = this.elevator.maxFloor - 1 - i;
      if (i === this.elevator.maxFloor - 1) {
        floor.classList.add('active');
      }
      section.appendChild(floor);
    }
  }

  updateActiveFloors(floors) {
    for (let i = 0; i < floors.length; i++) {
      floors[i].textContent = this.elevator.numberOfPeople;
      }
  }

  updateFloorsOnMoveUp(floors) {
    for (let i = floors.length -1; i >= 0; i--) {
      if (this.elevator.elevatorPosition == floors[i].id) {
        floors[i].classList.add('active');
        floors[i + 1].classList.remove('active');
      }
    }
  }

  updateFloorsOnMoveDown(floors) {
    for (let i = 0; i < floors.length; i++) {
      if (this.elevator.elevatorPosition == floors[i].id) {
        floors[i].classList.add('active');
        floors[i - 1].classList.remove('active');
      }
    }
  }
}


class ElevatorController {

  constructor() {
    this.elevatorModel = new ElevatorModel(10, 10);
    this.elevatorView = new ElevatorView(this.elevatorModel);
  }

  handleAddPeopleEvent() {
    this.elevatorModel.addPeople.bind(this.elevatorModel)();
    this.elevatorView.updateActiveFloors.bind(this.elevatorView)(floors);
  }

  handleRemovePeopleEvent() {
    this.elevatorModel.removePeople.bind(this.elevatorModel)();
    this.elevatorView.updateActiveFloors.bind(this.elevatorView)(floors);
  }

  handleMoveUpEvent() {
    this.elevatorModel.moveUp.bind(this.elevatorModel)();
    this.elevatorView.updateFloorsOnMoveUp.bind(this.elevatorView)(floors);
  }

  handleMoveDownEvent() {
    this.elevatorModel.moveDown.bind(this.elevatorModel)();
    this.elevatorView.updateFloorsOnMoveDown.bind(this.elevatorView)(floors);
  }

  handleEvents() {
    buttons[0].addEventListener('click', this.handleMoveUpEvent.bind(this));
    buttons[1].addEventListener('click', this.handleMoveDownEvent.bind(this));
    buttons[2].addEventListener('click', this.handleAddPeopleEvent.bind(this));
    buttons[3].addEventListener('click', this.handleRemovePeopleEvent.bind(this));
  }

}

let myElevator = new ElevatorController();
myElevator.elevatorView.drawFloors();
let floors = document.querySelectorAll('p');
myElevator.handleEvents();

