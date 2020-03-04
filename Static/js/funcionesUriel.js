// Function para obtener el token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {  
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

compile = async () => {

    let query = "";

    if(document.getElementById("textarea")!=null){
        query = document.getElementById("textarea").value;
        // console.log(query);
    }else{
        // let padre = document.getElementById("letras-contenido");
        query = document.getElementById("letras-contenido").textContent;
    }

    // console.log(query);
    


    $.ajax({ 
        type: 'POST',
        url: 'http://148.220.208.96:3000/',
        data: {query:query},
        success: function(data){
            // console.log(data);
            // console.log(Object.keys(data).length);

            if(Object.keys(data).length == 3){
                console.log("---ERROR---")

                let divResults = document.getElementById("salida-middle");
                divResults.innerHTML="";
                divResults.appendChild(document.createTextNode(data['english']));

                return 
            }

            let columnas = data['metaData'];
            let filas = data['rows'];

            // console.log(columnas.length);
            // console.log(filas.length);

            let tabla = document.createElement("table");
            let headers = document.createElement("tr");

            tabla.appendChild(headers);

            columnas.forEach(element => {
                // console.log(element['name'])
                let aux = document.createElement("th");
                aux.appendChild(document.createTextNode(element['name']));
                headers.appendChild(aux);
            });

            

            filas.forEach(element => {
                // console.log(element);
                let result = document.createElement("tr");
                tabla.appendChild(result);

                element.forEach(properties => {
                    // console.log(properties);

                    let aux = document.createElement("td");
                    aux.appendChild(document.createTextNode(properties))
                    result.appendChild(aux);
                });
                
                
            });

            let divResults = document.getElementById("salida-middle");
            divResults.innerHTML="";
            divResults.appendChild(tabla);
           
        },
        error: function(error){
            alert("Error", "Error de conectividad. Verifica tu conexion a Internet");


        },

        timeout: 5000
    });
}