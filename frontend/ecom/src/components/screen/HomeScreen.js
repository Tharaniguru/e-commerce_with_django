import React ,{useEffect, useState} from 'react';
import {Container} from "react-bootstrap";
import axios from 'axios';
import {Row,Col,Card} from 'react-bootstrap';
import '../../styles/HomeScreen.css'
import Products from '../products';


function HomeScreen() {
const[products,setProduct]=useState([])

useEffect(()=> {
  async function fetchproducts() {
    const {data} = await axios.get('/api/products/')
    setProduct(data)
    
  }
  fetchproducts()
},[])

  return (
    <Container>
      <br/>
      <h1>products</h1>
      

      <Row>
        {products.map((product)=>(
          <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
          
            <Products product={product} />
            
          </Col>
        ))}
      </Row>
    </Container>
  )
}

export default HomeScreen
