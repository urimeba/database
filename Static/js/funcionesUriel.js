var serverQuerys = 'http://148.220.52.132:3000/';
var serverWeb = 'http://127.0.0.1:8000/'

// Funcion para obtener la Cookie y mandarla al Back
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

// Funcion para compilar codigo SQL de Oracle
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

// Funcion para actualizar el numero de intentos en el HTML 
updateIntentos = (numeroIntentos) => {
    let divIntentos = document.getElementById("intentos");
    divIntentos.innerHTML="";
    divIntentos.innerText=numeroIntentos;
}

// FUNCIONES DEL EJERCICIO #1 DE LA UNIDAD 1
// Funcion para tomar el valor de un elemento SELECT
getTextSelect = (elementId) => {
    let select = document.getElementById(elementId);
    let res = select.options[select.selectedIndex].value;
    return res;
}

// Funcion para enviar el ejercicio al Back 
enviarEjercicio1_1 = () => {
    let res1 = getTextSelect("pregunta-1");
    let res2 = getTextSelect("pregunta-2");
    let res3 = getTextSelect("pregunta-3");
    let res4 = getTextSelect("pregunta-4");
    let res5 = getTextSelect("pregunta-5");
    let res6 = getTextSelect("pregunta-6");
    let res7 = getTextSelect("pregunta-7");
    let res8 = getTextSelect("pregunta-8");
    let res9 = getTextSelect("pregunta-9");
    let res10 = getTextSelect("pregunta-10");
    let token = getCookie('csrftoken');


    $.ajax({
            type: 'POST',
            url: serverWeb+'ejercicios/setEjercicio11',
            data: {
                csrfmiddlewaretoken: token,
                res1: res1,
                res2: res2,
                res3: res3,
                res4: res4,
                res5: res5,
                res6: res6,
                res7: res7,
                res8: res8,
                res9: res9,
                res10: res10,
            },
            success: function(data){
                alert(data['calificacion']);
                updateIntentos(data['intentos'])
            }
    });

}

// FUNCIONES DEL EJERCICIO #1 DE LA UNIDAD 2
// Funcion que retorna los elementos de una tabla (li's)
getTextLi = (elementoPadre) =>{
    let dic = [];

    for(let x=0; x<elementoPadre.children.length; x++){
        dic.push(elementoPadre.children[x].textContent)
    }

    return dic;
}

// Funcion para enviar el ejercicio al Back 
enviarEjercicio2_3 = () =>{
    let atributos = document.getElementById("sortable1");
    let videojuegos = document.getElementById("sortable2");
    let proveedores = document.getElementById("sortable3");
    let empleados = document.getElementById("sortable4");
    let clientes = document.getElementById("sortable5");

    let confirmacion = "";
    if(atributos.children.length>0){
        confirmacion = confirm("Parece que todavia tienes atributos sin colocar. ¿Deseas continuar?");

        if(!confirmacion){
            return;
        }
    }
    
    let token = getCookie('csrftoken');
    let atributosVideojuegos =  getTextLi(videojuegos);
    let atributosProveedores =  getTextLi(proveedores);
    let atributosEmpleados =  getTextLi(empleados);
    let atributosClientes =  getTextLi(clientes);


    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio21',
        data: {
            csrfmiddlewaretoken: token,
            atributosVideojuegos: JSON.stringify(atributosVideojuegos),
            atributosProveedores: JSON.stringify(atributosProveedores),
            atributosEmpleados: JSON.stringify(atributosEmpleados),
            atributosClientes: JSON.stringify(atributosClientes),
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos'])
        }
});



}