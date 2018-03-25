'use strict';

const buttons = document.querySelectorAll('button');
const section = document.querySelector('section');
const main = document.querySelector('main');
const divs = document.querySelectorAll('div');

function sendRequest(method, url, callback) {
  const xhr = new XMLHttpRequest;
  xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      const data = JSON.parse(xhr.response);
      callback(data);
    }
  };
  xhr.open(method, url);
  xhr.setRequestHeader('accept', 'application/json');
  xhr.send();
}

function listBookTitles(books) {
  buttons[0].disabled = true;
  let list = document.createElement('ol');
  section.appendChild(list);
  books.forEach((book) => {
    let listElement = document.createElement('li');
    listElement.textContent = book.book_name;
    list.appendChild(listElement);
  });
}

function showFullBookData(books) {
  buttons[1].disabled = true;
  let markup = '<table><thead><tr><th>Book Title</th> ' +
               '<th>Author name</th><th>Category</th> ' +
               '<th>Publisher\'s name</th><th>Price</th>' +
               '</tr></thead><tbody>';
  books.forEach((book) => {
    markup += `<tr>
                <td>${book.book_name}</td>
                <td>${book.aut_name}</td>
                <td>${book.cate_descrip}</td>
                <td>${book.pub_name}</td>
                <td>${book.book_price}</td>
               </tr>`;
  });
  markup += '</tbody></table>';
  main.innerHTML = markup;
}

function getQuery() {
  let form = document.querySelector('form');

  return '/books?' + [
    'category',
    'publisher',
    'plt',
    'pgt'
  ]
  .map((fieldName) => [fieldName, form.elements.namedItem(fieldName).value])
  .filter((nameValuePair) => nameValuePair[1] !== '')
  .map((queryParameter) => queryParameter.join('='))
  .join('&');
}

function showFilteredBookData(books) {
  let markup = '<table><thead><tr><th>Book Title</th> ' +
               '<th>Author name</th><th>Category</th> ' +
               '<th>Publisher\'s name</th><th>Price</th>' +
               '</tr></thead><tbody>';
  books.forEach((book) => {
    markup += `<tr>
                <td>${book.book_name}</td>
                <td>${book.aut_name}</td>
                <td>${book.cate_descrip}</td>
                <td>${book.pub_name}</td>
                <td>${book.book_price}</td>
               </tr>`;
  });
  markup += '</tbody></table>';
  divs[2].innerHTML = markup;
}

buttons[0].addEventListener('click', () => {
  sendRequest('GET', '/titles', listBookTitles);
});
buttons[1].addEventListener('click', () => {
  sendRequest('GET', '/books', showFullBookData);
});
document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault();
  sendRequest('GET', getQuery(), showFilteredBookData);
});
