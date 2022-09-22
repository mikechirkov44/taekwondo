const popup = document.querySelectorAll('#popup');

window.onclick = function(event) {
  popup.forEach(element => {
    if (event.target == element) {
      element.style.display = "none";
    } 
  });
}
