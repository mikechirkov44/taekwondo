function scrollFunction() {
    if (document.documentElement.scrollTop > 400) {
        document.getElementById("scroll__btn").style.display = "block";
    } else {
        document.getElementById("scroll__btn").style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

window.onscroll = function() {scrollFunction()};
