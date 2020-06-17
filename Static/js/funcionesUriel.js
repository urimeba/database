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

// Funcion para actualizar al calificacion
updateCalificacion = (calificacion) =>{
    calificacion = parseFloat(calificacion);
    let spanCalificacion = document.getElementById("calificacion_calificacion");
    spanCalificacion.textContent=calificacion.toFixed(2);;
}




// FUNCIONES DEL EJERCICIO #1 DE LA UNIDAD 1
// Funcion para tomar el valor de un elemento SELECT
getTextSelect = (elementId) => {
    let select = document.getElementById(elementId);
    let res = select.options[select.selectedIndex].value;
    return res;
}


enviarEjercicio0_1 = () =>{
    let confirmacion = confirm("¿Deseas enviar tu ejercicio?");
    if(!confirmacion){
        return;
    }

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
            url: serverWeb+'ejercicios/setEjercicio01',
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
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
            }
    });
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
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
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
enviarEjercicio2_1 = () =>{
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
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);

        }
    });
}

// FUNCIONES DEL EJERCICIO #2 DE LA UNIDAD 2
enviarEjercicio2_2 = () =>{
    let atributos = document.getElementById("sortable1");
    let oracle = document.getElementById("sortable2");
    let mysql = document.getElementById("sortable3");
    let postgres = document.getElementById("sortable4");

    let confirmacion = "";
    if(atributos.children.length>0){
        confirmacion = confirm("Parece que todavia tienes atributos sin colocar. ¿Deseas continuar?");
        if(!confirmacion){
            return;
        }
    }

    let token = getCookie('csrftoken');
    let atributosOracle =  getTextLi(oracle);
    let atributosmysql =  getTextLi(mysql);
    let atributospostgres =  getTextLi(postgres);

    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio22',
        data: {
            csrfmiddlewaretoken: token,
            atributosOracle: JSON.stringify(atributosOracle),
            atributosmysql: JSON.stringify(atributosmysql),
            atributospostgres: JSON.stringify(atributospostgres),
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);

        }
    });


}

// FUNCIONES DEL EJERCICIO #3 DE LA UNIDAD 2
enviarEjercicio2_3 = () =>{
    let atributos = document.getElementById("sortable1");
    let caracter = document.getElementById("sortable2");
    let numericos = document.getElementById("sortable3");
    let fecha = document.getElementById("sortable4");
    let objetos = document.getElementById("sortable5");

    let confirmacion = "";
    if(atributos.children.length>0){
        confirmacion = confirm("Parece que todavia tienes atributos sin colocar. ¿Deseas continuar?");
        if(!confirmacion){
            return;
        }
    }

    let token = getCookie('csrftoken');
    let atributosCaracter =  getTextLi(caracter);
    let atributosNumericos =  getTextLi(numericos);
    let atributosFecha =  getTextLi(fecha);
    let atributosObjetos =  getTextLi(objetos);

    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio23',
        data: {
            csrfmiddlewaretoken: token,
            atributosCaracter: JSON.stringify(atributosCaracter),
            atributosNumericos: JSON.stringify(atributosNumericos),
            atributosFecha: JSON.stringify(atributosFecha),
            atributosObjetos: JSON.stringify(atributosObjetos),
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);
        }
    });
}

// FUNCIONES DEL EJERCICIO #1 DE LA UNIDAD 3
enviarEjercicio3_1 = () =>{
    let body = document.getElementById("tabla").getElementsByTagName('tbody')[0];
    let dic = {};
    dic[body.rows[0].cells[0].textContent] = [];
    dic[body.rows[0].cells[1].textContent] = [];
    dic[body.rows[0].cells[2].textContent] = [];
    for(let x=1; x<body.rows.length; x++){
        dic[body.rows[0].cells[0].textContent].push(body.rows[x].cells[0].textContent);
        dic[body.rows[0].cells[1].textContent].push(body.rows[x].cells[1].textContent);
        dic[body.rows[0].cells[2].textContent].push(body.rows[x].cells[2].textContent);
    }

    let token = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio31',
        data: {
            csrfmiddlewaretoken: token,
            tabla: JSON.stringify(dic),
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);
        }
    });
}

enviarEjercicio3_2 = () =>{

    let confirmacion = confirm("¿Deseas enviar tu ejercicio?");
    if(!confirmacion){
        return;
    }

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
            url: serverWeb+'ejercicios/setEjercicio32',
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
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
            }
    });
}

enviarEjercicio4_1 = () =>{
    let confirmacion = confirm("¿Deseas enviar tu ejercicio?");
    if(!confirmacion){
        return;
    }

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
            url: serverWeb+'ejercicios/setEjercicio41',
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
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
            }
    });
}

enviarEjercicio4_2 = () =>{
    let atributos = document.getElementById("sortable1");
    let prestamo = document.getElementById("sortable5");

    let confirmacion = "";
    if(atributos.children.length>0){
        confirmacion = confirm("Parece que todavia tienes atributos sin colocar. ¿Deseas continuar?");
        if(!confirmacion){
            return;
        }
    }

    let token = getCookie('csrftoken');
    let atributosPrestamo =  getTextLi(prestamo);

    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio42',
        data: {
            csrfmiddlewaretoken: token,
            atributosPrestamo: JSON.stringify(atributosPrestamo),
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);
        }
    });
}

enviarEjercicio5_1 = () =>{
    let query = document.getElementById("query").textContent.trim()

    let token = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio51',
        data: {
            csrfmiddlewaretoken: token,
            query: query
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);
        }
    });

}

enviarEjercicio5_2 = () =>{
    let atributos = document.getElementById("sortable1");
    let notNull = document.getElementById("sortable2");
    let unique = document.getElementById("sortable3");
    let primaryKey = document.getElementById("sortable4");
    let foreignKey = document.getElementById("sortable5");
    let check = document.getElementById("sortable6");
    let defaultR = document.getElementById("sortable7");

    let confirmacion = "";
    if(atributos.children.length>0){
        confirmacion = confirm("Parece que todavia tienes atributos sin colocar. ¿Deseas continuar?");
        if(!confirmacion){
            return;
        }
    }

    let token = getCookie('csrftoken');
    let atributosNotNull =  getTextLi(notNull);
    let atributosUnique =  getTextLi(unique);
    let atributosPrimaryKey =  getTextLi(primaryKey);
    let atributosForeignKey =  getTextLi(foreignKey);
    let atributosCheck =  getTextLi(check);
    let atributosDefault =  getTextLi(defaultR);

    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio52',
        data: {
            csrfmiddlewaretoken: token,
            atributosNotNull: JSON.stringify(atributosNotNull),
            atributosUnique: JSON.stringify(atributosUnique),
            atributosPrimaryKey: JSON.stringify(atributosPrimaryKey),
            atributosForeignKey: JSON.stringify(atributosForeignKey),
            atributosCheck: JSON.stringify(atributosCheck),
            atributosDefault: JSON.stringify(atributosDefault),
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);
        }
    });

}

enviarEjercicio6_1 = () =>{
    let confirmacion = confirm("¿Deseas enviar tu ejercicio?");
    if(!confirmacion){
        return;
    }

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
            url: serverWeb+'ejercicios/setEjercicio61',
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
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
            }
    });

}

enviarEjercicio7_1 = () =>{
    let query = document.getElementById("query").textContent.trim()

    let token = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setEjercicio71',
        data: {
            csrfmiddlewaretoken: token,
            query: query
        },
        success: function(data){
            alert(data['calificacion']);
            updateIntentos(data['intentos']);
            updateCalificacion(data['calificacion_calificacion']);
        }
    });

}

enviarEjercicio7_2 = () =>{
    let confirmacion = confirm("¿Deseas enviar tu ejercicio?");
    if(!confirmacion){
        return;
    }

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
            url: serverWeb+'ejercicios/setEjercicio72',
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
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
            }
    });
}

enviarEjercicio8_1 = () =>{
    
    let confirmacion = confirm("¿Deseas enviar tu ejercicio?");
    if(!confirmacion){
        return;
    }

    let res1 = getTextSelect("pregunta-1");
    let res2 = getTextSelect("pregunta-2");
    let res3 = getTextSelect("pregunta-3");
    let res4 = getTextSelect("pregunta-4");
    let res5 = getTextSelect("pregunta-5");
    let res6 = getTextSelect("pregunta-6");
    let res7 = getTextSelect("pregunta-7");
    let res8 = getTextSelect("pregunta-8");
    let token = getCookie('csrftoken');

    $.ajax({
            type: 'POST',
            url: serverWeb+'ejercicios/setEjercicio81',
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
            },
            success: function(data){
                alert(data['calificacion']);
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
            }
    });
}

enviarEjercicio10_1 = () =>{
    
    let confirmacion = confirm("¿Deseas enviar tu ejercicio?");
    if(!confirmacion){
        return;
    }

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
            url: serverWeb+'ejercicios/setEjercicio91',
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
                updateIntentos(data['intentos']);
                updateCalificacion(data['calificacion_calificacion']);
            }
    });
}

actualizarCalificacion = (elementoHTML) =>{
    let idCalificacion = elementoHTML.dataset.idcalificacion;
    let calificacion = document.getElementById(idCalificacion).value;

    if(calificacion<0 || calificacion>10){
        alert("La calificacion debe ser mayor a 0 y menor a 10");
    }
    
    let token = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/setCalificacionAlumno',
        data: {
            csrfmiddlewaretoken: token,
            idCalificacion:idCalificacion,
            calificacion: calificacion
        },
        success: function(data){
            alert(data);
        }
    });
}

actualizarEjercicio = (elementoHTML) =>{
    let idEjercicio = elementoHTML.dataset.idejercicio;
    let estado = document.getElementById(idEjercicio).checked;

    let token = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: serverWeb+'ejercicios/actualizarEjercicio',
        data: {
            csrfmiddlewaretoken: token,
            idEjercicio:idEjercicio,
            estado: estado
        },
        success: function(data){
            alert(data);
        }
    });
    

}