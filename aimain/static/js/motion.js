var i = 0;
var button_list = document.getElementsByClassName("button-1");

//bar
function move() {
  if (i == 0) {
    j=0;
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 1;
    var id = setInterval(frame, 50);
    var para = document.getElementsByClassName("n")[0];
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
        para.innerText="No Error Found!";
        time=setInterval(() => {
          window.location.replace("http://localhost:8000/ai/Path/");
        }, 50);
      }
      
       else {
        width++;
        elem.style.width = width + "%";
    }
    }
  }
}
move();

//button animation
var a = setInterval(butt=>{
    button_list[j].style="background-color:green";
    if(j>=3){
        j=0;
        clearInterval(butt);
    }
    j++;
},1010);

