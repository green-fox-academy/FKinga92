'use strict';

function inputToPostObject() {
  let postTitle = document.querySelector('textarea').value;
  let postUrl = document.getElementById('url').value;
  if (postTitle === '' || postUrl === '') {
    alert('You cannot send a post with empty fields. Please enter a title and URL.');
    return;
  }
  return {
    "title": postTitle,
    "url": postUrl
  }
}

function getResponse() {
  let xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.DONE && xhr.status === 200) {
      document.location.href = 'main-page.html';
    }
  };
  xhr.open('POST', 'http://secure-reddit.herokuapp.com/simple/posts');
  xhr.setRequestHeader('accept', 'application/json');
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify(inputToPostObject()));
}

document.querySelector('button').addEventListener('click', getResponse);
