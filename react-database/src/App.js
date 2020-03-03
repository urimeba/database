import React from 'react';
import './static/css/indexEstilos.css'

function App() {
  return (
    <div className="App">
     
       <div id="Principal">
        <div className="container">
          <div className="row">
           <nav> 
           <div className="navbar-logo">Data<strong>Base</strong></div>
            <ul className="navbar-list">
              <li className="opciones">Inicio</li>
              <li className="opciones">Contenido</li>
              <li className="opciones">Herramientas</li>
            </ul>	
            <div className="navbar-profile">
              <div className="navbar-notification">
                <div className="navbar-notification-count">1</div>
              </div>
              <div className="navbar-notification navbar-avatar">
				        	<div className="navbar-picture">
                    <img src={require("./static/img/perfil.jpg")} alt="" className="img-profile"/>
                  </div>
			      	</div>
			
			      </div>
           </nav>
          </div>


    {/* Termina Nav */}
    <div id="mid-container">
    
      <div id="img-dashboard-container">
          <img src={require("./static/img/code.png")} alt="" className="img"/>
      </div>
      <div id="right-dashboard-container">
          <div id="right-dashboard-container-top">
            <div id="rectangulo"> </div>
            <h1 id="dashboard-title">Inicio</h1>
          </div>
          <div id="right-dashboard-container-middle">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt lacus ac ipsum bibendum fermentum. Fusce tempor dolor a metus egestas, ut finibus eros convallis.</p>
          </div>
         
      </div>

    </div>
    <div id="bottom-container">
        <div id="cuadros-container">
            <div className="dashboard-cuadros">

            </div>
            <div className="dashboard-cuadros">

            </div>
            <div className="dashboard-cuadros">

            </div>
            <div className="dashboard-cuadros">

            </div>
        </div>
    </div>


    <footer>
     <b>Centro de Desarrollo 2020. </b>
    </footer>



    </div>
  </div>
</div>
  );
}

export default App;
