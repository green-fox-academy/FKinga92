'use strict';

function isValidInput(postTitle, postUrl) {
  return (postTitle !== '' && postUrl !== '');
}

function inputToPostObject(postTitle, postUrl) {
    return {
      "title": postTitle,
      "url": postUrl,
      "timestamp": Date.now(),
      "owner": "anonymous"
    };
}

function submitPost() {
  let postTitle = document.querySelector('textarea').value;
  let postUrl = document.getElementById('url').value;
  let xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      document.location.href = 'main-page.html';
    }
  };
  xhr.open('POST', 'https://time-radish.glitch.me/posts');
  xhr.setRequestHeader('accept', 'application/json');
  xhr.setRequestHeader('content-type', 'application/json');
  if (isValidInput(postTitle, postUrl)) {
    xhr.send(JSON.stringify(inputToPostObject(postTitle, postUrl)));
  } else {
    alert('You cannot send a post with empty fields. Please enter a title and URL.');
  }
}

document.querySelector('button').addEventListener('click', submitPost);
