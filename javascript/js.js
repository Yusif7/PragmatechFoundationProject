
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
},3000);


//  WORKS SECTION MODALS
let close = document.getElementById("modal_close");
let modal = document.getElementById("works_modal");
let open = document.getElementById("open_modal");


open.onclick = function() {openFunction()};
function openFunction() {
modal.setAttribute("style","opacity: 1; visibility: visible;");
}
close.onclick = function() {closeFunction()};
function closeFunction() {
modal.setAttribute("style","opacity: 0; visibility: hidden;");
}
window.onclick = function(event){
if (event.target == modal){
modal.setAttribute("style","display: none;");
}
}

// PAGE SCROLL

