// script.js

const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');
const carrosselConteudo = document.querySelector('.carrossel-conteudo');
const totalItems = document.querySelectorAll('.item').length;
let currentIndex = 0;

function showItem(index) {
    carrosselConteudo.style.transform = `translateX(-${index * 100}%)`;
}

function goToNextItem() {
    if (currentIndex < totalItems - 1) {
        currentIndex++;
    } else {
        currentIndex = 0;
    }
    showItem(currentIndex);
}

// Set up automatic rotation every 3 seconds
const interval = setInterval(goToNextItem, 3000);

prevButton.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = totalItems - 1;
    }
    showItem(currentIndex);
});

nextButton.addEventListener('click', () => {
    goToNextItem();
});
