'use strict';

let body = document.querySelector('body');
let button = document.querySelector('button');

button.addEventListener('click', getResponse);

function getResponse() {
  let sentence = document.getElementById('sentence').value;
  let xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      console.log(JSON.parse(xhr.response));
    }
    if (xhr.status === 503) {
      console.log('Service Temporarily Unavailable');
    }
  };
  xhr.open('GET', 'https://yoda.p.mashape.com/yoda?sentence=You+will+learn+how+to+speak+like+me+someday.++Oh+wait.');
  xhr.setRequestHeader('X-Mashape-Key', 'wYyasdh3BZmsh1REIo5FUJZzqTpYp1VrYmHjsnqeaX5dkES2Zx');
  xhr.send();
}