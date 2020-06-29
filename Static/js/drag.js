const lista1 = document.getElementById("table-alumno");
const lista2 = document.getElementById("table-maestro");
const lista3 = document.getElementById("table-clase");
const lista4 = document.getElementById("table-resultado");


let paths = [],
    currentSVGPaths = [],
    currentColor,
    currentScroll = 0,
    initialScroll = 0,
    dif = 0,
    svgBool = false,
    lastScrollPx = 0,
    key = 1;
    pathsPx = {}

Sortable.create(lista1, {
    chosenClass: "seleccionado",
    group: {
        name: 'shared',
        pull: 'clone' // To clone: set pull to 'clone'
    },
    animation: 150,
    onAdd: function (e) {
        elemRect = e.to.parentElement.parentElement.getBoundingClientRect()
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        addFK(e)  

	},
});

Sortable.create(lista2, {
    chosenClass: "seleccionado",
    group: {
        name: 'shared',
        pull: 'clone'
    },
    animation: 150,
    onAdd: function(e) {
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        addFK(e)

    }
});

Sortable.create(lista3, {
    chosenClass: "seleccionado",
    group: {
        name: 'shared',
        pull: 'clone'
    },
    animation: 150,
    onAdd: function(e) {
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        addFK(e)
    }
});

Sortable.create(lista4, {
    chosenClass: "seleccionado",
    group: {
        name: 'shared',
        pull: 'clone'
    },
    animation: 150,
    onAdd: function(e) {
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        addFK(e)

    }
});


function addPaths(relation) {
    currentColor = generateRandomColor()
    svgBool = true
    lastScrollPx = initialScroll
    initialScroll = document.querySelector('#contenido-contenidoEjercicios').scrollTop
    addArrow(jQuery, window, document) // This file is in libs/jquer.html-svg-connect.js
    document.querySelector('#svgContainer').remove()
    document.querySelector('div.main').innerHTML = '<div id="svgContainer"></div>'
    $("#svgContainer").HTMLSVGconnect({
        stroke: '#' + currentColor,
        strokeWidth: 5,
        orientation: "auto",
        paths: [relation]
    })
    pathsPx[key] = initialScroll
    key++
    const path = document.querySelector('#svgContainer > svg > path')
    paths.push(path)
    adjustDifferentBottomPath()
}

function generateRandomColor() {
    currentColor = (Math.random()*0xFFFFFF<<0).toString(16)
    return currentColor
}

function adjustDifferentBottomPath() {
    // console.log('MY PATHS', currentSVGPaths)
    // currentSVGPaths.pop()
    console.log('ENTER HEREEE', paths.length)
    for(let i = 0; i < paths.length - 1; i++) {
        document.querySelector('#svgContainer > svg').appendChild(paths[i])
    }


    const pa = document.querySelectorAll('path')
    for(let i = 1; i < paths.length && paths.length > 1; i++) {
        let currentTraY = pathsPx[i] - initialScroll
        console.log(currentTraY)
        pa[i].style.transform = `translate(0, ${currentTraY}px)`
    }
}

function addFK(e){
   
        //Insertar abajo del drag
        var drag=e.target.parentElement;

        var fk=document.createElement("b");
        fk.classList.add("bold-fk");
        fk.innerText="(FK)";
        fk.style.color = '#'+currentColor
        var div=e.item.firstElementChild;
        // var padre=event.item;
         div.appendChild(fk);

         insertAfter(drag,e.item);
         e.item.classList.add("llaveForanea");
}
function insertAfter(e,i){ 
    if(e.nextSibling){ 
        e.parentNode.insertBefore(i,e.nextSibling); 
    } else { 
        e.parentNode.appendChild(i); 
    }
}



function reset(){
    var foraneas=document.getElementsByClassName("llaveForanea");
    paths = []
    currentSVGPaths = []
    const svgContainer = document.querySelector('#svgContainer > svg')
    if(svgContainer) {
        svgContainer.remove()
    }
  for (const iterator of foraneas) {
      iterator.remove();
  }
}

document.querySelector('#contenido-contenidoEjercicios').addEventListener('scroll', (e) => {
    if(svgBool) {
        currentScroll = document.querySelector('#contenido-contenidoEjercicios').scrollTop
        console.log(currentScroll, dif)
        dif = currentScroll - initialScroll
        document.querySelector('svg').style.bottom = `${dif}px`
    }
})