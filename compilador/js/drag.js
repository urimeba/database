const lista1 = document.getElementById("table-alumno");
const lista2 = document.getElementById("table-maestro");
const lista3 = document.getElementById("table-clase");
const lista4 = document.getElementById("table-xD");

let paths = []
let currentSVGPaths = []
let currentColor

Sortable.create(lista1, {
    chosenClass: "seleccionado",
    group: {
        name: 'shared',
        pull: 'clone' // To clone: set pull to 'clone'
    },
    animation: 150,
    onAdd: function (e) {
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
        sizePaths.push(0)
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        addFK(e)
    }
});

function addPaths(relation) {
    paths.push(relation)
    addArrow(jQuery, window, document) // This file is in libs/jquer.html-svg-connect.js

    currentSVGPaths.push(document.querySelectorAll('#svgContainer > svg > path'))

    resetSVGContainer()

    $("#svgContainer").HTMLSVGconnect({
        stroke: '#' + generateRandomColor(),
        strokeWidth: 5,
        orientation: "auto",
        paths: [relation]
    });

    if(document.querySelectorAll('#svgContainer > svg > path').length > 0) {
        addHTMLPaths()
    }
}

function resetSVGContainer() {
    document.querySelector('#svgContainer').remove()
    document.querySelector('div.main').innerHTML = '<div id="svgContainer"></div>'
}

function generateRandomColor() {
    currentColor = (Math.random()*0xFFFFFF<<0).toString(16)
    return currentColor
}

function addHTMLPaths() {
    for(let ArrPath of currentSVGPaths) {
        for(let path of ArrPath) {
            document.querySelector('#svgContainer > svg').appendChild(path)
        }
    }
}

function existRelation(relation) {
    return paths.findIndex(el => el.start === relation.start && el.end === relation.end) >= 0
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

function removeLastPathElement() {
    const paths = Array.from(document.querySelectorAll('path')).slice(-1)
    if(paths.length > 0) {
        paths.pop().remove()
        paths.pop()
        currentSVGPaths.pop()
    }
}

function reset(){
    var foraneas=document.getElementsByClassName("llaveForanea");

    removeLastPathElement()
  for (const iterator of foraneas) {
      iterator.remove();
  }
}