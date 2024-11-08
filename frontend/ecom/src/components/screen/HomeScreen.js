/* eslint-disable no-unused-vars */
import React ,{useEffect, useState} from 'react';
import {Container} from "react-bootstrap";
import axios from 'axios';
import {Row,Col,Card} from 'react-bootstrap';
import '../../styles/HomeScreen.css'
import Products from '../products';
import { listProducts } from '../../actions/productActions';
import { useDispatch,useSelector } from 'react-redux';


function HomeScreen() {


const dispatch =useDispatch()
const productsList = useSelector((state)=>state.productsList);

const {error , loading ,products} =productsList

useEffect(()=> {
  dispatch(listProducts())
},[dispatch])

  return (
    <Container>
      <br/>
      <h1>products</h1>
      {
        loading?(
          <h2>loading...</h2>
        ):error?(
          <h3>{error}</h3>
        ):(
          <Row>
        {products.map((product)=>(
          <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
          
            <Products product={product} />
            
          </Col>
        ))}
      </Row>
        )
      }

      
    </Container>
  );
}

export default HomeScreen
