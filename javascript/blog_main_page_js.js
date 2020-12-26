// Blog Menu settings
let blogright = document.querySelector('.blog_right');
let nav = document.querySelector('.nav');
let logo = document.querySelector('.logo');
let rightref = document.querySelector(".back");



window.onscroll = function() {scrollFunction()};

function scrollFunction() {
if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    blogright.style.visibility = "visible";
    nav.style.background = "white";
    logo.style.color = "black";
    rightref.style.visibility = "visible";
    rightref.style.transition = "all 0.8s ease 0s";
} else {
    blogright.style.visibility = "hidden";
    nav.style.background = '';
    logo.style.color = "white";
    rightref.style.visibility = "hidden";
    rightref.style.transition = "0s";
}
}

// PRELOADER 

document.body.onload = function(){
    setTimeout(function(){
        let preloader = document.querySelector("#preloader");
        if (!preloader.classList.contains("done")){
            preloader.classList.add("done");
        }
    },700)
}