let images = document.querySelectorAll('.images');
let thumbnails = document.querySelector('footer').querySelectorAll('img');
let arrowLeft = document.querySelectorAll('img')[0];
let arrowRight = document.querySelector('.arrow-right').getElementsByTagName('img')[0];
let current = 0;

function reset() {
  images.forEach(function(item) {
    item.style.display = 'none';
  });
  for (let i = 0; i < thumbnails.length; i++) {
    deActivateThumbnail(i);
  }
}

function activateThumbnail(index) {
  thumbnails[index].classList.add('active');
}

function deActivateThumbnail(index) {
  if (index === -1) {
    index = images.length -1;
  }
  if (index === images.length) {
    index = 0;
  }
  thumbnails[index].classList.remove('active');
}

function startSlide() {
  reset();
  images[0].style.display = 'block';
  activateThumbnail(0);
}

function selectSlide(index) {
  reset();
  images[index].style.display = 'block';
  activateThumbnail(index);
  current = index;
}

function slideLeft() {
  reset();
  images[current - 1].style.display = 'block';
  activateThumbnail(current - 1);
  deActivateThumbnail(current);
  current--;
}

function slideRight() {
  reset();
  images[current + 1].style.display = 'block';
  activateThumbnail(current + 1);
  deActivateThumbnail(current);
  current++;
}

arrowLeft.addEventListener('click', function() {
  if (current === 0) {
    current = images.length;
  }
  slideLeft();
});

arrowRight.addEventListener('click', function() {
  if (current === images.length - 1) {
    current = -1;
  }
  slideRight();
});


for (let i = 0; i < thumbnails.length; i++) {
  thumbnails[i].addEventListener('click', function() {
    selectSlide(i);
  });
}

startSlide();