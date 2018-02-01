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

function getUrlWithQueryParameters() {
  const radioButtons = document.querySelectorAll('input[type="radio"]');
  let queryParameters = `/search?q=${document.querySelector('form').elements.namedItem('lincence').value}`;
  if (radioButtons[0].checked === true) {
    queryParameters += '&police=1';
  } else if (radioButtons[1].checked === true) {
    queryParameters += '&diplomat=1';
  }
  return queryParameters;
}

function createTableWithHead() {
  const table = document.createElement('table');
  document.querySelector('body').appendChild(table);
  const tableHead = document.createElement('thead');
  table.appendChild(tableHead);
  table.appendChild(document.createElement('tbody'));
  let headerContents = ['Licence plate', 'Brand', 'Model', 'Color', 'Year'];
  for (let i = 0; i < headerContents.length; i++) {
    let header = document.createElement('th');
    header.textContent = headerContents[i];
    tableHead.appendChild(header);
  }
}

function showAllCarsWithSameType(brandName) {
  resetResultArea();
  sendRequest('GET', `/search/${brandName}`, showFilteredResult);
}

function createTableContent(lincencePlates) {
  const responseProperties = ['licence', 'brand', 'model', 'color', 'year'];
  lincencePlates.data.forEach((car) => {
    const newTableRow = document.createElement('tr');
    document.querySelector('tbody').appendChild(newTableRow);
    for (let i = 0; i < responseProperties.length; i++) {
      const newTableData = document.createElement('td');
      if (i === 1) {
        newTableData.textContent = `[${car[responseProperties[i]]}]`;
        newTableData.style.cursor = 'pointer';
        newTableData.addEventListener('click', () => {
          showAllCarsWithSameType(car[responseProperties[i]]);
        });
      } else {
        newTableData.textContent = car[responseProperties[i]];
      }
      newTableRow.appendChild(newTableData);
    } 
  });
}

function showFilteredResult(lincencePlates) {
  if (lincencePlates.result === 'error') {
    let errorTextSpan = document.createElement('span');
    errorTextSpan.textContent = 'Sorry, the submitted licence plate is not valid';
    document.querySelector('body').appendChild(errorTextSpan);
  } else if (lincencePlates.data.length === 0) {
    let noMatchTextSpan = document.createElement('span');
    noMatchTextSpan.textContent = 'Sorry, no match found.';
    document.querySelector('body').appendChild(noMatchTextSpan);
  } else {
    createTableWithHead();
    createTableContent(lincencePlates);
  } 
}

function resetResultArea() {
  const table = document.querySelector('table');
  if (table !== null) {
    table.parentNode.removeChild(table);
  }
  const span = document.querySelector('span');
  if (span !== null) {
    span.parentNode.removeChild(span);
  }
}

document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault();
  resetResultArea();
  sendRequest('GET', getUrlWithQueryParameters(), showFilteredResult);
});

