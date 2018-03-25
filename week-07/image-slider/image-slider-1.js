const imageDecriptions = [
  {title: 'Sunny beach'},
  {title: 'Christmas lights'},
  {title: 'Tiger'},
  {title: 'Airplane at sundown'},
  {title: 'The road to Zen'},
  {title: 'Windmills'},
  {title: 'Clear sky and white sand'},
  {title: 'Field of poppies'}
];

const descriptionTexts = [
  'Praesent sed eros justo. Nulla augue mi, sagittis consequat congue sodales, consectetur eget tortor.',
  'Cras sed metus ut tellus suscipit tincidunt in at erat. Donec rhoncus, enim bibendum semper fermentum, sem massa dictum velit, vitae vestibulum nibh ligula a lacus.',
  'Mauris orci dui, semper in porta at, condimentum in eros. Duis a tempor tellus. Quisque eu lectus varius sapien dignissim laoreet.',
  'In faucibus ligula urna, nec varius leo vulputate sed. Mauris pulvinar consectetur nibh lacinia laoreet. Morbi et ultrices massa.',
  'Aenean sit amet ultrices nunc. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.',
  'Nulla bibendum est magna, a mattis leo rhoncus sit amet. Mauris tempor libero vitae enim rhoncus posuere.'
];

let main = document.querySelector('main');
let rightAside = document.querySelector('.arrow-right');
let footer = document.querySelector('footer');

function createContainerSection() {
  let newSection = document.createElement('section');
  newSection.setAttribute('class', 'images');
  main.insertBefore(newSection, rightAside);
  return newSection;
}

function createImage(index) {
  let newImage = document.createElement('img');
  newImage.src = `images/${index + 1}.jpg`;
  newImage.alt = imageDecriptions[index].title.toLowerCase();
  return newImage;
}

function createChildSection(index) {
  let newChildSection = document.createElement('section');
  newChildSection.setAttribute('class', 'description');
  if (imageDecriptions[index].title === 'Christmas lights') {
    newChildSection.classList.add('christmas');
  }
  return newChildSection;
}

function createH2(index) {
  let newH2 = document.createElement('h2');
  newH2.innerText = imageDecriptions[index].title;
  return newH2;
}

function createParagraph() {
  let randomDescription = descriptionTexts[Math.floor(Math.random() * descriptionTexts.length)];
  let newParagraph = document.createElement('p');
  newParagraph.innerText = randomDescription;
  return newParagraph;
}

function createPhotoViewer(index) {
  let newSection = createContainerSection();
  let newImage = createImage(index);
  newSection.appendChild(newImage);
  let newChildSection = createChildSection(index);
  newSection.appendChild(newChildSection);
  let newH2 = createH2(index);
  newChildSection.appendChild(newH2);
  let newParagraph = createParagraph();
  newChildSection.appendChild(newParagraph);
}

function createFooterSection() {
  let newFooterSection = document.createElement('section');
  newFooterSection.classList.add('thumbnails');
  footer.appendChild(newFooterSection);
  return newFooterSection;
}

function createFooterImage(index) {
  let newFooterImage = document.createElement('img');
  newFooterImage.src = `images/${index + 1}-small.jpg`;
  newFooterImage.alt = imageDecriptions[index].title.toLowerCase();
  return newFooterImage;
}

function createFooterSpan(index) {
  let newFooterSpan = document.createElement('span');
  newFooterSpan.innerText = imageDecriptions[index].title;
  return newFooterSpan;
}

function createThumbnails(index) {
  let newFooterSection = createFooterSection();
  let newFooterImage = createFooterImage(index);
  newFooterSection.appendChild(newFooterImage);
  let newFooterSpan = createFooterSpan(index);
  newFooterSection.appendChild(newFooterSpan);
}

function createHTMLStructure() {
  imageDecriptions.forEach((item, index) => {
    createPhotoViewer(index);
    createThumbnails(index);
  });
}

function reset() {
  images.forEach((item) => {
    item.style.display = 'none';
  });
  thumbnails.forEach((thumbnail, index) => {
    deactivateThumbnail(index);
  });
}

function activateThumbnail(index) {
  thumbnails[index].classList.add('active');
}

function deactivateThumbnail(index) {
  if (index === -1) {
    index = images.length -1;
  } else if (index === images.length) {
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
  current--;
}

function slideRight() {
  reset();
  images[current + 1].style.display = 'block';
  activateThumbnail(current + 1);
  current++;
}

createHTMLStructure();
let images = document.querySelectorAll('.images');
let thumbnails = document.querySelector('footer').querySelectorAll('img');
let arrowLeft = document.querySelectorAll('img')[0];
let arrowRight = document.querySelector('.arrow-right').getElementsByTagName('img')[0];
let current = 0;

arrowLeft.addEventListener('click', () => {
  if (current === 0) {
    current = images.length;
  }
  slideLeft();
});

arrowRight.addEventListener('click', () => {
  if (current === images.length - 1) {
    current = -1;
  }
  slideRight();
});

thumbnails.forEach((thumbnail, index) => {
  thumbnail.addEventListener('click', () => {
    selectSlide(index);
  });
});

window.addEventListener('keyup', (event) => {
  if (event.keyCode === 37) {
    if (current === 0) {
      current = images.length;
    }
    slideLeft();
  }
  if (event.keyCode === 39) {
    if (current === images.length - 1) {
      current = -1;
    }
    slideRight();
  }
});

startSlide();
