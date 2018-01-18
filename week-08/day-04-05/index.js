'use strict';

let myMain = document.querySelector('main');

function getResponse() {
  let xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.DONE && xhr.status === 200) {
      let posts = JSON.parse(xhr.response).posts;
      posts.forEach(function(post, index, posts) {
        createPost(posts, index);
      });
    }
  };
  xhr.open('GET', 'http://secure-reddit.herokuapp.com/simple/posts');
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
  spanLink.innerText = posts[index].url.replace('http://', '').replace('https://', '');
  spanLink.href = posts[index].url;
  spanLink.target = '_blank';
  span.appendChild(spanLink);
}

function createSubmitInfo(posts, index, contentDiv) {
  let submitInfo = document.createElement('p');
  let minutes = Math.floor(((Date.now() - posts[index].timestamp) / 1000) / 60);
  submitInfo.innerHTML = `submitted ${minutes} minutes ago by anonymous`;
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

function createPost(posts, index) {
  let containerDiv = createContainerDiv(posts, index);
  let voteDiv = createVoteDiv(containerDiv);
  createVoteDivContent(posts, index, voteDiv);
  let contentDiv = createContentDiv(containerDiv);
  let title = createTitleParagraph(contentDiv);
  createTitleLink(posts, index, title);
  createSpan(posts, index, title);
  createSubmitInfo(posts, index, contentDiv);
  createPostModificationLinks(contentDiv);
}

window.addEventListener('load', (event) => {
  getResponse();
});