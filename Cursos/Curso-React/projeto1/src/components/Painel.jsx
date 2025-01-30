import '../estilos/painel.css'

function Painel() {
    return (
        <article>
            <div>
                <h2>Alunos</h2>
                <img src="imagens/group.png" alt=""/>
                <p>10</p>
                <p>Total de Alunos cadastrados</p>
            </div>
            <div>
                <h2>Integrantes</h2>
                <img src="imagens/groups.png" alt=""/>
                <p>45</p>
                <p>Total de Integrantes ativos</p>
            </div>
            <div>
                <h2>Partituras</h2>
                <img src="imagens/parts.png" alt=""/>
                <p>635</p>
                <p>Total de Partituras cadastradas</p>
            </div>
        </article>
    )
}

export default Painel