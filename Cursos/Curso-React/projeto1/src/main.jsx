import { createRoot } from 'react-dom/client'
import Header from './components/Header.jsx'
import Nav from './components/Nav.jsx'

createRoot(document.querySelector('body')).render(
  <body>
    <Nav/>
    <Header/>
  </body>
)
