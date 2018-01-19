'use strict';

let myMain = document.querySelector('main');

function getInitialResponse() {
  let xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      let posts = (JSON.parse(xhr.response)).posts;
      posts.splice(50);
      createPost(posts);
      setUpVoteAction();
      setDownVoteAction();
    }
  };
  xhr.open('GET', 'https://time-radish.glitch.me/posts');
  xhr.setRequestHeader('accept', 'application/json');
  xhr.send();
}

function createContainerDiv(posts, index) {
  let containerDiv = document.createElement('div');
  containerDiv.setAttribute('id', posts[index].id);
  myMain.appendChild(containerDiv);
  return containerDiv;
}

function createVoteDiv(containerDiv) {
  let voteDiv = document.createElement('div');
  voteDiv.classList.add('vote');
  containerDiv.appendChild(voteDiv);
  return voteDiv;
}

function createVoteDivContent(posts, index, voteDiv) {
  let upArrowDiv = document.createElement('div');
  upArrowDiv.classList.add('arrow-up');
  voteDiv.appendChild(upArrowDiv);

  let scoreParagraph = document.createElement('p');
  scoreParagraph.innerText = posts[index].score;
  voteDiv.appendChild(scoreParagraph);

  let downArrowDiv = document.createElement('div');
  downArrowDiv.classList.add('arrow-down');
  voteDiv.appendChild(downArrowDiv);
}

function createContentDiv(containerDiv) {
  let contentDiv = document.createElement('div');
  contentDiv.classList.add('content');
  containerDiv.appendChild(contentDiv);
  return contentDiv;
}

function createTitleParagraph(contentDiv) {
  let title = document.createElement('p');
  title.classList.add('title');
  contentDiv.appendChild(title);
  return title;
}

function createTitleLink(posts, index, titleParagraph) {
  let titleLink = document.createElement('a');
  titleLink.innerText = posts[index].title;
  titleLink.href = posts[index].url;
  titleParagraph.appendChild(titleLink);
}

function createSpan(posts, index, titleParagraph) {
  let span = document.createElement('span');
  titleParagraph.appendChild(span);

  let spanLink = document.createElement('a');
  spanLink.innerText = (posts[index].url != null)
    ? posts[index].url.replace('http://', '').replace('https://', '')
    : '';
  spanLink.href = posts[index].url;
  spanLink.target = '_blank';
  span.appendChild(spanLink);
}

function createSubmitInfo(posts, index, contentDiv) {
  let submitInfo = document.createElement('p');
  let minutes = Math.floor(((Date.now() - posts[index].timestamp) / 1000) / 60);
  let postOwner = (posts[index].owner != null)
    ? posts[index].owner
    : 'anonymous';
  submitInfo.innerHTML = `submitted ${minutes} minutes ago by ${postOwner}`;
  contentDiv.appendChild(submitInfo);
}

function createPostModificationLinks(contentDiv) {
  let unorderedList = document.createElement('ul');
  contentDiv.appendChild(unorderedList);

  let listElement1 = document.createElement('li');
  unorderedList.appendChild(listElement1);
  let modifyLink = document.createElement('a');
  modifyLink.innerText = 'modify';
  modifyLink.href = '#';
  listElement1.appendChild(modifyLink);

  let listElement2 = document.createElement('li');
  unorderedList.appendChild(listElement2);
  let removeLink = document.createElement('a');
  removeLink.innerText = 'remove';
  removeLink.href = '#';
  listElement2.appendChild(removeLink);
}

function createPost(posts) {
  posts.forEach(function(post, index, posts) {
    let containerDiv = createContainerDiv(posts, index);
    let voteDiv = createVoteDiv(containerDiv);
    createVoteDivContent(posts, index, voteDiv);
    let contentDiv = createContentDiv(containerDiv);
    let title = createTitleParagraph(contentDiv);
    createTitleLink(posts, index, title);
    createSpan(posts, index, title);
    createSubmitInfo(posts, index, contentDiv);
    createPostModificationLinks(contentDiv);
  });
}

function updateScore(button, direction) {
  let postId = button.parentElement.parentElement.id;

  let putRequest = new XMLHttpRequest();
  putRequest.onreadystatechange = function() {
    if (putRequest.readyState === XMLHttpRequest.DONE && putRequest.status === 200) {
      let updatedPost = JSON.parse(putRequest.response);
      document.getElementById(`${updatedPost.id}`)
      .getElementsByClassName('vote')[0]
      .querySelector('p').textContent = updatedPost.score;
    }
  };
  putRequest.open('PUT', `https://time-radish.glitch.me/posts/${postId}/${direction}vote`);
  putRequest.setRequestHeader('accept', 'application/json');
  putRequest.send();
}

function setUpVoteAction() {
  let buttons = document.querySelectorAll('div[class="arrow-up"]'); 
  buttons.forEach(function(button) {
    button.addEventListener('click', function() {
      updateScore(button, 'up');
    });
  });
}

function setDownVoteAction() {
  let buttons = document.querySelectorAll('div[class="arrow-down"]'); 
  buttons.forEach(function(button) {
    button.addEventListener('click', function() {
      updateScore(button, 'down');
    });
  });
}

window.addEventListener('load', (event) => {
  getInitialResponse();
});