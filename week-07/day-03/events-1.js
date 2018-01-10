// Turn the party on and off by clicking the button. (the whole page)

function turnOn() {
  document.querySelector('div').classList.toggle('party');
}

document.querySelector('button').addEventListener('click', turnOn);
