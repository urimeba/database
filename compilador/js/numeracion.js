window.addEventListener('load', numerar, false);
function numerar() {

var contenedor= document.getElementById("numeracion");

for(x=1;x<=20;x++){
    var item=document.createElement('div');
    item.classList.add("numero");
    contenedor.appendChild(item);
   
    console.log("Item "+x);
}
}