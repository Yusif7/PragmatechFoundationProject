
// Header slider
// Create list
let slidelist = ['DEVELOPER', 'CODER', 'GAMER', 'PROGRAMMER', 'FREELANCER', 'ANALYST'];
//select needed div
let hobbies = document.querySelector('.hobbi');
// Calc
let i = 0;
// Show time 
window.setInterval(function(){
hobbies.innerHTML = slidelist[i];
i++;
// Break 
if(i == slidelist.length){
i = 0
}
},2500);




//  WORKS SECTION MODALS

let modalsref = document.querySelectorAll("#open_modal");
let html = document.querySelector("#html");
html.className
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
let closeref = document.querySelectorAll("#modal_close");
closeref.forEach(function(ref){
    ref.onclick = function(){
        // Works_modal classli parent tap ve style teyin et 
        let modal = (ref.closest(".works_modal").setAttribute("style","opacity: 0; visibility: hidden;"));
        //sehife scroll geri qaytar
        html.setAttribute("style", "overflow: scroll;");
    }
    
});
// Bu niye islemir ozumde bilmirem her seyi duzdu ama islemir nerviden partliyiram , derdini tapsaz mene deyin zehmet olmasa 
window.onclick = function(event){
    if (event.target.className === '.works_modal'){
        event.target.setAttribute("style","opacity: 0; visibility: hidden;");
    }
};





// Menu settings
//Deyisim olan variable yaradildi
let navbarright = document.querySelector('.navbarright');
let nav = document.querySelector('.nav');
let logo = document.querySelector('.logo')

// Ekran surusmesi funksiyasi teyin olundu
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    // Body taga scroll px teyin olundu
if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
navbarright.style.visibility = "visible";
nav.style.background = "white";
logo.style.color = "black";
} else {
navbarright.style.visibility = "hidden";
nav.style.background = '';
logo.style.color = "white";
}
}