let myMain = document.querySelector('main');

let xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4 && xhr.status === 200) {
    let gifs = JSON.parse(xhr.response).data;
    console.log(gifs);
    for (let i = 0; i < gifs.length; i++) {
      createImage(i, gifs).addEventListener('click', function() {
        displayGif(event.target, gifs, i);
      });
    }
  }
};
xhr.open('GET', "https://api.giphy.com/v1/gifs/search?api_key=RKxv0jprqPz4VnafELIdBm8k1NL6DaNO&q=funny+dog&limit=16");
xhr.send();

function createImage(index, data) {
  let image = document.createElement('img');
  image.src = data[index]['images']['original_still']['url'];
  image.style.width = data[index]['images']['original_still']['width'];
  image.style.height = data[index]['images']['original_still']['height'];
  myMain.appendChild(image);
  return image;
}

function displayGif(img, data, index) {
  img.src = data[index]['images']['original']['url'];
}
