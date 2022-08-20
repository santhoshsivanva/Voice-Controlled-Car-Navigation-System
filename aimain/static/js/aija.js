var audio1 = document.getElementById("carSound");
var on = document.getElementById("mai");
var start_bb = document.getElementById("neww");
var audio2 = document.getElementById("startSound");

function myPlay(){
    audio1.play();
    audio2.play();
    function onn(){
        on.innerText="ON";
    }
    onn() //closure
}




start_bb.addEventListener("click",myPlay);