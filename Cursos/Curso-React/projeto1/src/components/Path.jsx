import React from 'react';
import {useLocation, useParams } from 'react-router-dom';
import Painel from './Painel.jsx';
import Alunos from './Alunos.jsx';
import Integrantes from './Integrantes.jsx';
import Partituras from './Partituras.jsx';
import Agenda from './Agenda.jsx';
function Path() {
    const location = useLocation();
    const { id } = useParams();
    if(location.pathname == '/') {
        return <Painel/>;
    }
    if(location.pathname ==='/Alunos') {
        return <Alunos/>;
    }
    if(location.pathname ==='/Integrantes') {
        return <Integrantes/>;
    }
    if(location.pathname ==='/Partituras') {
        return <Partituras/>;

    }
    if(location.pathname ==='/Agenda') {
        return <Agenda/>;
    }
    if (id) {
        return <h1>'{id}' Not Found</h1>
    } 
}

export default Path