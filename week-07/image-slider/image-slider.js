let images = document.querySelectorAll('.images');
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

startSlide();