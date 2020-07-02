const PLAY_BUTTON = document.querySelector('#play'),
  CONTAINER_BOTTOM = document.querySelector('#container-bottom'),
  LOADER_ANIMATION = document.querySelector('#loader-animation'),
  TABLES_CONTAINER = document.querySelector('#tablas-container')


var code;

var mime = 'text/x-mariadb';
// get mime type
if (window.location.href.indexOf('mime=') > -1) {
  mime = window.location.href.substr(window.location.href.indexOf('mime=') + 5);
}
code= CodeMirror.fromTextArea(document.getElementById('code'), {
  mode: mime,
  indentWithTabs: true,
  smartIndent: true,
  lineNumbers: true,
  matchBrackets : true,
  autofocus: true,
  extraKeys: {"Ctrl-Space": "autocomplete"},
 
});



function limpiar(){
  console.log(code.setValue(''));
}

function addLoaderAnimation() {
  PLAY_BUTTON.setAttribute('disabled', '')
  PLAY_BUTTON.classList.add('disabled')
  setTimeout(() => {
    addLoaderElementToContainer()
    CONTAINER_BOTTOM.classList.add('container-opacity')
  }, 400)
}

function addLoaderElementToContainer() {
  TABLES_CONTAINER.innerHTML = 
    `<div class="loader-container">
      <div id="loader-animation" class="lds-facebook"><div></div><div></div><div></div></div>
    </div>`
}

function removeHelperAttributes() {
  CONTAINER_BOTTOM.classList.remove('container-opacity')
  PLAY_BUTTON.classList.remove('disabled')
  PLAY_BUTTON.removeAttribute('disabled')
}

function removeLoaderAnimation() {
  TABLES_CONTAINER.innerHTML = ''
}

function addToast(message, status) {
  const toast = document.getElementById("snackbar");

  if(status === 'successfully') {
    toast.classList.add('successfully')
  } else if(status === 'warning') {
    toast.classList.add('warning')
  } else if(status === 'error'){
    toast.classList.add('error')
  }

  toast.classList.add('show');
  toast.innerText = message

  setTimeout(function(){ toast.className = toast.classList.remove('show'); }, 3000);
}