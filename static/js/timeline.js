const slides = document.querySelectorAll('.slide');
const sliderLine = document.querySelector('.timeline-slider-line')
const years = document.querySelectorAll('.timeline-year');
let active = 0;
let width;

function init() {
    width = document.querySelector('.timeline-slider').offsetWidth;
    sliderLine.style.width = 1+(width * slides.length) + 'px';
};

init();

// document.querySelector('.controls-next').onclick = () => {
//     years[active].classList.remove('active-year');
//     slides[active].classList.remove('active');
//     if (active + 1 == slides.length) {
//         active = 0;
//     } else {
//         active++;
//     }
//     years[active].classList.add('active-year');
//     slides[active].classList.add('active');
//     rollSlides()
// }

// document.querySelector('.controls-prev').onclick = () => {
//     years[active].classList.remove('active-year');
//     slides[active].classList.remove('active');
//     if (active - 1 < 0) {
//         active = 2;
//     } else {
//         active--;
//     }
//     years[active].classList.add('active-year');
//     slides[active].classList.add('active');
// }

function rollSlides() {
    sliderLine.style.transform = 'translate(-' + active * width + 'px)';
}

function nextSlide() {
    years[active].classList.remove('active-year');
    if (active + 1 == slides.length) {
        active = 0;
    } else {
        active++;
    }
    years[active].classList.add('active-year');
    rollSlides();
}

function prevSlide() {
    years[active].classList.remove('active-year');
    if (active - 1 < 0) {
        active = 2;
    } else {
        active--;
    }
    years[active].classList.add('active-year');
    rollSlides();
}

function clearActive() {
    years.forEach((year) => {
        year.classList.remove('active-year');
    });
}

document.querySelector('.controls-next').addEventListener('click', () => {
    nextSlide();
});
document.querySelector('.controls-prev').addEventListener('click', () => {
    prevSlide();
});

years.forEach((year) => {
    year.addEventListener('click', () => {
        clearActive();
        year.classList.add('active-year');
        active = year.value;
        rollSlides();
    })
})
