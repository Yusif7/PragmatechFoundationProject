// Blog Menu settings
let blogright = document.querySelector('.blogright');
let nav = document.querySelector('.nav');
let logo = document.querySelector('.logo')


window.onscroll = function() {scrollFunction()};

function scrollFunction() {
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



//  WORKS SECTION MODALS

let modalsref = document.querySelectorAll("#open_modal");
let html = document.querySelector("#html");
console.log(modalsref, html);

// #open_modal id olan taglarin bir bir gotur
modalsref.forEach(function(ref){
    // Eger her hansi birine click olacaqsa
    ref.onclick = function(){
        // Hemin tagin data-modal atributunu cagir
        let modal = ref.getAttribute("data-modal");
        //Hemin tag stil teyin et
        document.getElementById(modal).setAttribute("style","opacity: 1; visibility: visible;");
        // Kenarda iki dene scroll olmasin deye modal acilanda sehife scrol olmasin
        html.setAttribute("style", "overflow: hidden;");
    }
    
});
//Baglanma icon teyin edilsin
let closeref = document.querySelectorAll("#close_modal");
closeref.forEach(function(ref){
    ref.onclick = function(){
        // Works_modal classli parent tap ve style teyin et 
        let modal = (ref.closest(".blog_modal").setAttribute("style","opacity: 0; visibility: hidden;"));
        //sehife scroll geri qaytar
        html.setAttribute("style", "overflow: scroll;");
    }
    
});