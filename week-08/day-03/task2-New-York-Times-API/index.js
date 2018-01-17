let myMain = document.querySelector('main');

let xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4 && xhr.status === 200) {
    let articles = JSON.parse(xhr.response).response.docs;
    console.log(articles);
    articles.forEach(function(article, index) {
      createList(index, articles);
    });
    }
};
xhr.open('GET', 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=moon+landing+apollo+11&fq=apollo&page=37&sort=oldest&api-key=8b4c94cbe93d4cfab8e984c3ed6d18e9');
xhr.send();

let neededFields = ['snippet', 'pub_date'];

function createList(index, data) {
  let unorderedList = document.createElement('ul');
  myMain.appendChild(unorderedList);
  for (let i = 0; i < 3; i++) {
    let listElement = document.createElement('li');
    if (i > 0) {
      listElement.textContent = data[index][neededFields[i - 1]];
      unorderedList.appendChild(listElement);
    }
    else {
      unorderedList.appendChild(listElement);
      listElement.appendChild(createLink(index, data));
    }    
  }
}

function createLink(index, data) {
  let link = document.createElement('a');
  link.href = data[index]['web_url'];
  link.target = "_blank";
  link.textContent = data[index]['headline']['main'];
  return link;
}