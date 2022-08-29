"use strict"

const numbers = document.querySelectorAll("span.promo-list-item__red")

function render() {
  let interval = setInterval(() => {
    numbers.forEach(element => {
      let newnum = getRandomInt(0, +element.innerHTML+5);
      element.classList.add("visible");
      return element.innerHTML = newnum;
    });
  }, 40);
  setTimeout(() => {
    window.clearInterval(interval);
    numbers.forEach(element => {
        return element.innerHTML = element.dataset.value;
    });
  }, 800);
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

render(numbers)