const lista1 = document.getElementById("table-alumno");
const lista2 = document.getElementById("table-maestro");
const lista3 = document.getElementById("table-clase");
const lista4 = document.getElementById("table-xD");

const paths = []
const currentSVGPaths = []
const shapePositions = []

let coordX = coordY = 0

Sortable.create(lista1, {
    chosenClass: "seleccionado",
    group: {
        name: 'shared',
        pull: 'clone' // To clone: set pull to 'clone'
    },
    animation: 150,
    onAdd: function (e) {
        elemRect = e.to.parentElement.parentElement.getBoundingClientRect()
        console.log(elemRect)

        const fromPosition = e.from.parentElement.parentElement.dataset.position,
            toPosition = e.to.parentElement.parentElement.dataset.position;
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        setCoordinates(parseInt(fromPosition), parseInt(toPosition))
        shapePositions.push({coordX, coordY})
        createShape(`${coordX - 5}px`, `${coordY - 5}px`)
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
        console.log(e.to.parentElement.parentElement.getBoundingClientRect())
        const fromPosition = e.from.parentElement.parentElement.dataset.position,
            toPosition = e.to.parentElement.parentElement.dataset.position;
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        setCoordinates(parseInt(fromPosition), parseInt(toPosition))
        shapePositions.push({coordX, coordY})
        createShape(`${coordX - 5}px`, `${coordY - 5}px`)
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
        console.log(e.to.parentElement.parentElement.getBoundingClientRect())
        const fromPosition = e.from.parentElement.parentElement.dataset.position,
            toPosition = e.to.parentElement.parentElement.dataset.position;
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        setCoordinates(parseInt(fromPosition), parseInt(toPosition))
        shapePositions.push({coordX, coordY})
        createShape(`${coordX - 5}px`, `${coordY - 5}px`)
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
        console.log(e.to.parentElement.parentElement.getBoundingClientRect())
        const fromPosition = e.from.parentElement.parentElement.dataset.position,
            toPosition = e.to.parentElement.parentElement.dataset.position;
        addPaths({ start: '#'+e.from.id, end: '#'+e.to.id, strokeWidth: 1 })
        setCoordinates(parseInt(fromPosition), parseInt(toPosition))
        shapePositions.push({coordX, coordY})
        createShape(`${coordX - 5}px`, `${coordY - 5}px`)
    }
});

function addPaths(relation) {
    if(!existRelation(relation)) {
        paths.push(relation)
        addArrow(jQuery, window, document) // This file is in libs/jquer.html-svg-connect.js
        if(document.querySelectorAll('#svgContainer > svg > path').length > 0) {
            currentSVGPaths.push(document.querySelectorAll('#svgContainer > svg > path'))
        }
        document.querySelector('#svgContainer').remove()
        document.querySelector('div.main').innerHTML = '<div id="svgContainer"></div>'
        $("#svgContainer").HTMLSVGconnect({
            stroke: '#'+(Math.random()*0xFFFFFF<<0).toString(16),
            strokeWidth: 5,
            orientation: "auto",
            paths: [relation]
        });

        if(document.querySelectorAll('#svgContainer > svg > path').length > 0) {
            addHTMLPaths()
        }
    }
}

function setCoordinates(fromPos, toPos) {
    if(fromPos < toPos) {
        coordX = endX
        coordY = endY
    } else {
        coordX = startX
        coordY = startY
    }

    console.log(startX, startY, coordX, coordY)
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

function createShape(x, y) {
    console.log(x, y)
    const div = document.createElement('div')
    div.classList.add('shape')
    div.style.left = x
    div.style.top = y
    document.body.appendChild(div)
}