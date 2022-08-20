var ok_ = document.getElementById("but_ok");
var container = document.getElementsByClassName("container")[0];



function trans(){
    container.style="transform:scale(2,2)"
    container.className="container animate__animated animate__fadeOutLeft animate__delay-0.5s";

}

ok_.addEventListener("click",trans);
