// Menu settings
//Deyisim olan variable yaradildi
let blogright = document.querySelector('.blogright');
let nav = document.querySelector('.nav');
let logo = document.querySelector('.logo')

console.log(blogright, nav, logo);
// Ekran surusmesi funksiyasi teyin olundu
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    // Body taga scroll px teyin olundu
if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    blogright.style.visibility = "visible";
    nav.style.background = "white";
    logo.style.color = "black";
} else {
    blogright.style.visibility = "hidden";
    nav.style.background = '';
    logo.style.color = "white";
}
}