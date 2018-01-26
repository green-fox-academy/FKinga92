'use strict';

const button = document.querySelector('button');
const body = document.querySelector('body');

function ajax(method, url, callback) {
  const xhr = new XMLHttpRequest;
  xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      const data = JSON.parse(xhr.response);
      callback(data);
    }
  };
  xhr.open('GET', url);
  xhr.setRequestHeader('accept', 'application/json');
  xhr.send();
}

function listBookTitles(books) {
  button.disabled = true;
  let list = document.createElement('ul');
  body.appendChild(list);
  books.forEach(book => {
    let listElement = document.createElement('li')
    listElement.textContent = book.book_name
    list.appendChild(listElement);
  });
}

button.addEventListener('click', () => {
  ajax('GET', 'http://localhost:8080/titles', listBookTitles);
});


