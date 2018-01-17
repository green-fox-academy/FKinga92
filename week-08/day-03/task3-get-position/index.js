'use strict';

let body = document.querySelector('body');
let button = document.querySelector('button');
let clickCounter = 0;
button.addEventListener('click', getResponse);

function getResponse() {
  let city = document.getElementById('location').value.split(' ').join('+');
  requestCityLocation(city);
  createMap(city);
  clickCounter++;
}

function displayCoordinates(city) {
  if (clickCounter <= 1) {
    let locationPar = document.createElement('p');
    locationPar.textContent = 'Your city\'s coordinates: ' + city.lat + ', ' + city.lon;
    body.appendChild(locationPar);
  } else {
    document.querySelector('p').textContent = 'Your city\'s coordinates: ' + city.lat + ', ' + city.lon;
  }
}

function requestCityLocation(city) {
  let xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      let cityPosition = JSON.parse(xhr.response).Results[0];
      displayCoordinates(cityPosition);
    }
  };
  xhr.open('GET', `https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=${city}`);
  xhr.setRequestHeader('X-Mashape-Key', 'wYyasdh3BZmsh1REIo5FUJZzqTpYp1VrYmHjsnqeaX5dkES2Zx');
  xhr.send();
}

function createMap(city) {
  if (clickCounter < 1) {
    let map = document.createElement('iframe');
    map.width = '600';
    map.height = '450';
    map.frameborder = '0';
    map.style = 'border: 0';
    map.src = `https://www.google.com/maps/embed/v1/place?key=AIzaSyBFf7IRxT68e-9DlS0SlkPv2hb8pp_7M4U&q=${city}`;
    body.appendChild(map);
  } else {
    document.querySelector('iframe').src = `https://www.google.com/maps/embed/v1/place?key=AIzaSyBFf7IRxT68e-9DlS0SlkPv2hb8pp_7M4U&q=${city}`;
  }
}
