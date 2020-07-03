var graf=Morris.Bar ({
    element: 'myfirstchart',
    xkey: 'mapname',
    ykeys: ['value','value2','value3'],
    labels: ['Calificación 1','Calificación 2','Calificación 3'],
    barColors:[ ' #ec7063 ',' #5499c7 ',' #607D8B ']
   
  });

  var datos= [
    {mapname: 'Ej. 1', value: 10, value2: 3, value3: 3},
    {mapname: 'Ej. 2', value: 4, value2: 4, value3: 3},
    {mapname: 'Ej. 3', value: 10, value2: 10, value3: 3},
    {mapname: 'Ej. 4', value: 10, value2: 10, value3: 3},
    {mapname: 'Ej. 5', value: 10, value2: 10, value3: 3},
    {mapname: 'Ej. 6', value: 10, value2: 10, value3: 3},
    {mapname: 'Ej. 7', value: 10, value2: 10, value3: 3},
    {mapname: 'Ej. 8', value: 10, value2: 10, value3: 3},
    {mapname: 'Ej. 9', value: 10, value2: 10, value3: 3},
    
  ];
  graf.setData(datos);
