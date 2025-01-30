import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Path from './Path';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Path/>} />
        <Route path='/Alunos' element={<Path/>} />
        <Route path='/Integrantes' element={<Path/>} />
        <Route path='/Partituras' element={<Path/>} />
        <Route path='/Agenda' element={<Path/>} />
        <Route path='/:id' element={<Path/>} />
      </Routes>
    </Router>
  );
}

export default App;