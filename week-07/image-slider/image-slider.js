let images = document.querySelectorAll('.images');
let arrowLeft = document.querySelectorAll('img')[0];
let arrowRight = document.querySelector('.arrow-right').getElementsByTagName('img')[0];
let current = 0;

function reset() {
  images.forEach(function(item) {
    item.style.display = 'none';
  })
}

function startSlide() {
  reset();
  images[0].style.display = 'block';
}

function slideLeft() {
  reset();
  images[current - 1].style.display = 'block';
  current--;
}

function slideRight() {
  reset();
  images[current + 1].style.display = 'block';
  current++;
}

arrowLeft.addEventListener('click', function() {
  if (current === 0) {
    current = images.length;
  }
  slideLeft();
})

arrowRight.addEventListener('click', function() {
  if (current === images.length - 1) {
    current = -1;
  }
  slideRight();
})


startSlide();