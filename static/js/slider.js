"use strict"

let slideIndex = 1
showSlide(slideIndex)

function moveSlide(n) {
    showSlide(slideIndex += n);
}

function currentSlide (n) {
    showSlide(slideIndex = n);
}

function showSlide (n) {
    const slides = document.getElementsByClassName("slider-item");
    const dots = document.getElementsByClassName("slider-item__dot")
    if (n>slides.length) {
        slideIndex = 1;
    }
    if (n<1) {
        slideIndex = slides.length;
    }
    for (let i=0; i<slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (let i=0; i<dots.length; i++) {
        dots[i].classList.remove("active-dot");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].classList.add("active-dot");
}