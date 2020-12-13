

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



let close = document.getElementById("modal_close");
let modal = document.getElementById("works_modal");
let open = document.getElementById("open_modal");

console.log(modal);
console.log(open);
console.log(close);

open.onclick = function() {openFunction()};
function openFunction() {
modal.setAttribute("style","display: block; transition: all .8s ease 0s;");
}
close.onclick = function() {closeFunction()};
function closeFunction() {
modal.setAttribute("style","display: none; transition: all .8s ease 0s;");
}


