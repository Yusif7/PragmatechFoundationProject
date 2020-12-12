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
},3000)