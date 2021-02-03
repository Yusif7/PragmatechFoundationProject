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



//  bLOGS MODALS

let modalsref = document.querySelectorAll("#open_modal");
let html = document.querySelector("html");
let prev = document.querySelector(".prev")
let next = document.querySelector(".next")


// #open_modal id olan taglarin bir bir gotur
modalsref.forEach(function(ref){  
    ref.onclick = function(){
        let modal = ref.getAttribute("data-modal");
        document.getElementById(modal).setAttribute("style","opacity: 1; visibility: visible;");
        html.setAttribute("style", "overflow: hidden;");
        let src = ref.querySelector("img").getAttribute("src");
        console.log(src);
    } 
});
//Baglanma icon teyin edilsin
let closeref = document.querySelectorAll("#close_modal");
closeref.forEach(function(ref){
    ref.onclick = function(){
        let modal = (ref.closest(".blog_modal").setAttribute("style","opacity: 0; visibility: hidden;"));
        html.setAttribute("style", "overflow: scroll;");
    }
});

// PRELOADER 

document.body.onload = function(){
    setTimeout(function(){
        let preloader = document.querySelector("#preloader");
        if (!preloader.classList.contains("done")){
            preloader.classList.add("done");
        }
    },500)
}

