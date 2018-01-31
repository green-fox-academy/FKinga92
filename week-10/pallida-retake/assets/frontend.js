'use strict';

function sendRequest(method, url, callback) {
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      const data = JSON.parse(xhr.response);
      callback(data);
    }
  };
  xhr.open(method, url);
  xhr.setRequestHeader('accept', 'application/json');
  xhr.send();
}

function showTable(responseData) {
  const clothes = responseData.clothes;
  const tableBody = document.querySelector('tbody');
  const clothsProperties = ['item_name', 'manufacturer', 'category', 'size', 'unit_price'];
  clothes.forEach((clothingPiece) => {
    const tableRow = document.createElement('tr');
    tableBody.appendChild(tableRow);
    for (let i = 0; i < 5; i++) {
      const tableData = document.createElement('td');
      tableData.textContent = clothingPiece[clothsProperties[i]];
      tableRow.appendChild(tableData);
    }
  });
}

function getQuery() {
  const form = document.querySelector('form');
  const clothesSelect = form.elements.namedItem('clothes');
  const sizeSelect = form.elements.namedItem('size');
  return '/price-check/?' + [
    ['item', clothesSelect.options[clothesSelect.selectedIndex].text],
    ['size', sizeSelect.options[sizeSelect.selectedIndex].text],
    ['quantity', parseInt(document.querySelector('input').value, 10)]
  ]
  .map(queryParameter => queryParameter.join('='))
  .join('&');
}

function displayMessage(responseData) {
  const resultMessage = document.querySelector('p');
  if (responseData.result === 'ok') {
    resultMessage.textContent = `The items can be ordered at the total price of: ${responseData.total_price}`;
    resultMessage.setAttribute('data-status', 'ok');
  } else {
    resultMessage.textContent = responseData.result;
    resultMessage.setAttribute('data-status', 'error');
  }
}


document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault();
  sendRequest('GET', getQuery(), displayMessage);
});

window.addEventListener('load', () => {
  sendRequest('GET', '/warehouse', showTable);
});
