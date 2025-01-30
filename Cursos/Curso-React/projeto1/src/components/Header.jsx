import App from "./App"
import esconder from "../scripts"
import  '../estilos/index.css'
function Header() {
  return (
    <main>
      <header>
        <div className="container">
          <button onClick={esconder}></button>
          <form action="#">
            <input type="search" className="barra-pesquisa" name="psq" id="ipsq" placeholder="Buscar.."/>
            <input type="submit" className="botao-pesquisa" value=""/>
          </form>
          <div>
            <button></button>
            <div>
              <p>Otávio Santiago</p>
              <p>Administrador</p>
            </div>
          </div>
        </div>
        <div className="titulo">
          <h1>Banda Santa Cecilia</h1>
          <p>Jaraguá - GO</p>
        </div>
      </header>

      <App/>

    </main>
  )
}

export default Header