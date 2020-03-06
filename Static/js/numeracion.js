// var contadorLinea=11;
// var contadorTecla=10;

// window.addEventListener('load', cambiarTextArea, false);
// function cambiarTextArea() {

//     var letras=document.getElementsByClassName('letras-contenido');
  
//     for (const letra of letras) {
//         letra.addEventListener('click',alerta);
//     }
  
    
// }
// function alerta(e){
 
// if(e.target.nodeName === 'DIV') {
//     var contenidoTextA=e.target.innerHTML.split(' ').map(e=>e.trim(' ')).filter(e=>e!="");
//     agregar(span(contenidoTextA), e.target);
    
// }

 
// }

// function span(contenidoTextA){
//     var cont = [];

  
//     for(let e of contenidoTextA){
//         var item=document.createElement('span');
//         item.innerText= e+'';
//         cont.push(item);
//     } 

//     return(cont);

// }
// function agregar(arreglo,target){
//     var text=document.createElement('TEXTAREA');
//     text.addEventListener('keydown', sumar)
//     text.classList.add("textarea");
//     text.value='\n\n\n\n\n\n\n\n\n'; 
  
    
//     // for (const iterator of arreglo) {
        
       

//     // }
//     target.innerHTML="";
//     target.appendChild(text);
//     text.focus();
    


// }

// function sumar(e) {
  
//     if(e.key === 'ArrowUp') {
//         contadorTecla--;
//     }
//     if(e.key === 'ArrowDown') {
//         contadorTecla++;
//         console.log('hola');
//     }

//     if(e.key === 'Enter') {
//         // var incremento=e.target.parentElement.parentElement.offsetHeight+19;
//         // e.target.parentElement.parentElement.style.height=incremento+'px';
//         var incremento=e.target.offsetHeight + 19;
//         e.target.style.height=incremento+ 'px';
//         e.target.parentElement.height=incremento + 'px';
        
//     //    e.target.rows++;
//         var item=document.createElement('div');
//         item.classList.add('number');
//         var padre=document.getElementById('numbers-container');
//         padre.appendChild(item);


//         item.innerText=contadorLinea;
//        contadorLinea++;
//        contadorTecla++;
//     }
//     if(e.key === 'Backspace') {

//         if(contadorLinea>2){
//             quitarLinea(e.target)
//             e.target.parentElement.parentElement.parentElement.children[0].lastElementChild.remove();
//             var decremento=e.target.offsetHeight-19;
//             e.target.style.height=decremento+'px';
                
//             e.target.parentElement.parentElement.parentElement.style.height= decremento+'px';
//             contadorLinea--;
            
//         }
//         else{
//             console.log('guapo');
//         }
//     }
//     console.log(contadorTecla);
// }

// function quitarLinea(text) {
//     console.log(text.value.split('\n'), contadorLinea)
// }

var editor=CodeMirror.fromTextArea(document.getElementById("code"), {
    lineNumbers: true,
    mode: "htmlmixed"
  });