var contadorLinea=2;

window.addEventListener('load', cambiarTextArea, false);
function cambiarTextArea() {

    var letras=document.getElementsByClassName('letras-contenido');
    
  
    for (const letra of letras) {
        letra.addEventListener('click',alerta);
    }
  
    
}
function alerta(e){
    
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
    text.addEventListener('keydown', sumar)
    text.classList.add("textarea");
    text.setAttribute("id", "textarea");
    
    for (const iterator of arreglo) {
        text.innerText += iterator.innerText + ' ';
       
        
    }
    target.innerHTML="";
    target.appendChild(text);
    text.focus();
    


}

function sumar(e) {
  
    
    

    if(e.key === 'Enter') {
        var incremento=e.target.parentElement.parentElement.offsetHeight+19;
        e.target.parentElement.parentElement.style.height=incremento+'px';
    //    e.target.rows++;
        var item=document.createElement('div');
        item.classList.add('number');
        var padre=document.getElementById('numbers-container');
        padre.appendChild(item);


        item.innerText=contadorLinea;
       contadorLinea++;
    }
    if(e.key === 'Backspace') {
        if(quitarLinea(e.target.value)) {
            var decremento=e.target.parentElement.parentElement.offsetHeight-19;
            e.target.parentElement.parentElement.style.height=decremento+'px';
            e.target.parentElement.parentElement.parentElement.parentElement.children[0].lastElementChild.remove()
        contadorLinea--;
        }
    }
}

function quitarLinea(str) {
    return str.split('\n').pop() === ''
    
}

