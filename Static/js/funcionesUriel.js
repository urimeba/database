var server = 'http://148.220.52.132:3000/';
window.onload = function(){
    getLastUnity();
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {  
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }}}
    return cookieValue;
}

compile = async () => {
    let query = code.getValue();

    $.ajax({ 
        type: 'POST',
        url: server,
        data: {query:query},
        success: function(data){

            let divResults = document.getElementById("tablas-container");
            divResults.innerHTML="";

            if(Object.keys(data).length == 3){
                divResults.appendChild(document.createTextNode(data['english']));
                return
            }

            let columnas = data['metaData'];
            let filas = data['rows'];

            let tabla = document.createElement("table");
            let headers = document.createElement("tr");
            tabla.appendChild(headers);

            columnas.forEach(element => {
                let aux = document.createElement("th");
                aux.appendChild(document.createTextNode(element['name']));
                headers.appendChild(aux);
            });

            filas.forEach(element => {
                let result = document.createElement("tr");
                tabla.appendChild(result);

                element.forEach(properties => {
                    let aux = document.createElement("td");
                    aux.appendChild(document.createTextNode(properties))
                    result.appendChild(aux);
                });
            });

            divResults.appendChild(tabla);
           
        },
        error: function(error){ 
            alert("Error de conectividad. Verifica tu conexion a Internet");
        },
        timeout: 5000
    });
}

getLastUnity = () => {
    try {
        let unities = document.getElementsByClassName("u2");
        unities[unities.length-1].setAttribute("class", "u1");

        for(let x=0; x<unities.length; x++){
            unities[x].addEventListener("click", function(){
                changeUnity(this.id);
            })
        }
    } catch (error) {
        console.log(error);
    }
}

changeUnity = async (id) => {
    let idUnity = id;
    let token = getCookie('csrftoken');

    $.ajax({ 
        type: 'POST',
        url: 'http://127.0.0.1:8000/changeUnity',
        data: {idUnity: idUnity, csrfmiddlewaretoken: token},
        success: function(data){
            // console.log(data);

            let title = document.getElementById("title")
            let description = document.getElementById("description");
            let presentation = document.getElementById("contenido-contenidoEjercicios");

            title.innerHTML = "";
            description.innerHTML="";
            presentation.innerHTML=data['presentation'];

            title.appendChild(document.createTextNode(data['title']));
            description.appendChild(document.createTextNode(data['description']));
        }
    });

    let unities = document.getElementsByClassName("u1");
    unities[0].setAttribute("class", "u2");

    let new_unity = document.getElementById(id);
    new_unity.setAttribute("class", "u1");
    new_unity.removeEventListener("click", changeUnity);

    let new_unities = document.getElementsByClassName("u2");
    for(let x=0; x<new_unities.length; x++){
        new_unities[x].addEventListener("click", function(){
            changeUnity(this.id);
        })
    }
}


getEjercicio = (id) =>{
    let idEjercicio = id.split('-');
    idEjercicio = idEjercicio[1];

    let token = getCookie('csrftoken');
    $.ajax({ 
        type: 'POST',
        url: 'http://127.0.0.1:8000/getEjercicio',
        data: {idEjercicio: idEjercicio, csrfmiddlewaretoken: token},
        success: function(data){
            // console.log(data);
            let divPadre = document.getElementById('contenido-contenidoEjercicios');
            divPadre.innerHTML='';
            divPadre.innerHTML=data;
        }
    });

}

enviarEjercicio2 = (id) =>{
    let tabla = document.getElementById("tabla-"+id);
    let filas = tabla.getElementsByTagName("tr");
    let respuestas = []
    let estado = true;

    for(let x=0; x<filas.length; x++){

        let res = filas[x].getElementsByTagName("td");

        for(let y=0; y<res.length; y++){
            // console.log(res[y].innerText);
            let txt = res[y].innerText;
            txt.trim;
            // console.log(txt);
            respuestas.push(txt);
        }

    }

    // console.log(respuestas);

    for(let x=0; x<respuestas.length; x++){
        // console.log(respuestas[x]);
        if(respuestas[x]==''){
            estado=false;
        }
    }

    let confirmacion;
    if(!estado){
        confirmacion = confirm("Parece que tu ejercicio no esta completo. Deseas mandarlo de todos modos");
    }

    if(estado || confirmacion){
        let token = getCookie('csrftoken');
        $.ajax({ 
            type: 'POST',
            url: 'http://127.0.0.1:8000/setRespuestas',
            data: {respuestas: JSON.stringify(respuestas), idEjercicio:id, csrfmiddlewaretoken: token},
            success: function(data){
                // console.log(data);
                alert(data)
            }
        });

    }

    


   


}