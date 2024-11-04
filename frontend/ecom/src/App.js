import React from 'react'
import {Container} from 'react-bootstrap'
import NavBar from './components/NavBar'
import Footer from './components/Footer'

function App() {
  return (
    <div>
     <>
     <div>
      <NavBar />

      <Container>
        <h1>welcome to STSmart</h1>
      </Container>
     <Footer />
     </div>
     
     </>
    </div>
  )
}

export default App
