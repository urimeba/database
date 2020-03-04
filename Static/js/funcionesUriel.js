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
    let query = document.getElementById("textarea").value;

    if(query.length==0){
        alert("Debes escribir algo en la consola");
        return
    }

    
    let request = await fetch('http://148.220.52.121:3000', {
        method: 'POST',
        headers: {
            'Content-Type': 'applicaction/json',
            'Accep': 'applicaction/json'
        },
        body: JSON.stringify({ query: "Select * from hr.employees" }),
        credentials: 'include'
    })
    let response = await request.json()

    console.log(response)

    

    // $.ajax({ 
    //     type: 'POST',
    //     url: 'http://148.220.52.121:3000',
    //     data: {query:query},
    //     success: function(data){
    //         console.log(data);
            
    //     }
    // });
}