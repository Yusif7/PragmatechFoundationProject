
// Header slider
// Create list
let slidelist = ['DEVELOPER', 'CODER', 'GAMER', 'PROGRAMMER', 'FREELANCER', 'ANALYST'];
//select needed div
let hobbies = document.querySelector('.hobbi');
// Calc
let i = 1;
//Display gorsenen element
hobbies.innerHTML = slidelist[0];
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
let wmodals = document.querySelectorAll(".works_modal")

// Bu niye islemir ozumde bilmirem her seyi duzdu ama islemir nerviden partliyiram , derdini tapsaz mene deyin zehmet olmasa 
window.onclick = function(event){
    if (event.target == wmodals){
        wmodals.target.setAttribute("style","opacity: 0; visibility: hidden;");
    }
};





// Menu settings
//Deyisim olan variable yaradildi
let navbarright = document.querySelector('.navBarRight');
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



// PRELOADER 
// Body tag funksiya teyin olunur
document.body.onload = function(){
    //Funksiyanin isleme araligi teyin olunur
    setTimeout(function(){
        //Preloade tag secilir
        let preloader = document.querySelector("#preloader");
        // Eger preloader taginda done class teyin olunmayibsa
        if (!preloader.classList.contains("done")){
            // Done classinin preloader tagina elave et
            preloader.classList.add("done");
        }
    },700)
}



// Work image filter
function app(){
    const filterName = document.querySelectorAll(".filter1");
    const filterContent = document.querySelectorAll(".works");
    // Work ve content deyerini gebul eden funksiyanin yazilmasi
    function filter (work, items) {
        // Content daxiline giririk
        items.forEach(item => {
            // Content terkibinde is filterNamede olan klass var mi?
            const isItemFiltered = item.classList.contains(work);
            // Hamisini gosteren class 
            const showAll = work.toLowerCase() === "all";
            //Eger content filterNamede klassina beraberdise hide klassinin sil
            if (isItemFiltered){
                item.classList.remove("anime")
                item.classList.remove("hide")
                // Eger beraber deyilse hide klasini elave et
            }else{
                item.classList.add("anime")
            }
            // Eger filterName all secilibse hide hamisindan sil
            if (showAll){
                item.classList.remove("anime")
                item.classList.remove("hide")
                item.setAttribute("style", "transition:all 0.5s ease 0s;")
            }

        })
    }
    // Is kategoriyalari
    filterName.forEach(name => {
        name.addEventListener("click", function(){
            // Kategoriyalar daxilinde yaradilan data-filter klassinin deyerini gotur 
            const currentWork = name.dataset.filter;
            //Filter funksiyasinin tetbiq et
            filter(currentWork, filterContent);
        })
    })
    // Animasiyadan sonra yeniden strukturun qurulmasi
    filterContent.forEach(content => {
        // Visible hidden olandan sonra animasiya seklinde
        content.ontransitionend = function(){
            // Anime klassi tetbiq edilenden sonra check et eger obyektde anime klassi varsa ona hide klassini elave et
            if(content.classList.contains("anime")){
                content.classList.add("hide")
            }
        }
    })
}
// Umumi funksiyani cagir
app()