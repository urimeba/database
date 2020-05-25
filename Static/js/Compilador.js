

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