window.addEventListener('load', cambiarTextArea, false);
function cambiarTextArea() {

    var letras=document.getElementsByClassName('letras-contenido');
  
    for (const letra of letras) {
        letra.addEventListener('click',alerta);
    }
  
    
}
function alerta(e){
    console.log(e.target.nodeName)
if(e.target.nodeName === 'DIV') {
    var contenidoTextA=e.target.innerHTML.split(' ').map(e=>e.trim(' ')).filter(e=>e!="");
    agregar(span(contenidoTextA), e.target);

}

 
}

function span(contenidoTextA){
    var cont = [];

  
    for(let e of contenidoTextA){
        var item=document.createElement('span');
        item.innerText=e;
        cont.push(item);
    } 

    return(cont);

}
function agregar(arreglo,target){
    var text=document.createElement('TEXTAREA');
    text.addEventListener('keypress', sumar)
    text.classList.add("textarea");
    
    for (const iterator of arreglo) {
        text.innerText += iterator.innerText + ' ';
        console.log(iterator);
        
    }
    target.innerHTML="";
    target.appendChild(text);
    


}

function sumar(e) {
    if(e.key === 'Enter') {
        insertAfter(document.createElement('div'), e);
    }
}

function insertAfter(e,i){ 
    console.log(e, i)
    if(e.nextSibling){ 
        e.parentElement.insertBefore(i,e.nextSibling); 
    } else { 
        e.parentElement.appendChild(i); 
    }
}
    