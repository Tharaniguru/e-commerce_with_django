import React ,{useEffect, useState} from 'react';
import { Row,Col,Image,ListGroup,Button,Card,Container } from 'react-bootstrap'
import { Link ,useParams} from 'react-router-dom'
import Rating from '../Rating'
import axios from 'axios'



function ProductScreen({params}) {
    const {id} =useParams()
    const[products ,setProduct]=useState([])
    useEffect(()=> {
      async function fetchproducts() {
        const {data} = await axios.get(`/api/product/${id}`);
        setProduct(data)
        
      }
      fetchproducts()
    },[])

  return (
    <Container>
        <div>
      <Link to='/' className='btn btn-dark my-3'>Go Back</Link>
      <Row>
        <Col md={6}>
          <Image src={products.image} alt={products.name} fluid />
        </Col>
    

    <Col md={3}>
          <ListGroup variant="flush">
            <ListGroup.Item>
              <h3>{products.productname}</h3>
            </ListGroup.Item>
            <ListGroup.Item>
            <Rating
               value={products.rating} 
               text={`${products.numReview} reviews`}
               color={"#f8e825"}
               />
            </ListGroup.Item>
            <ListGroup.Item>Brand: {products.productbrand} </ListGroup.Item>
            
            <ListGroup.Item>Description: {products.productinfo}</ListGroup.Item>
          </ListGroup>
    </Col>

    <Col md={3}>
          <Card>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <Row>
                  <Col>Price:</Col>
                  <Col>
                    <strong>Rs. {products.price}</strong>
                  </Col>
                </Row>
              </ListGroup.Item>
              <ListGroup.Item>
                <Row>
                  <Col>Status:</Col>
                  <Col>
                    {products.stockcount > 0 ? "In Stock" : "Out of Stock"}
                  </Col>
                </Row>
              </ListGroup.Item>
            <ListGroup.Item>
                <Button className='btn-block btn-success' disabled={products.stockcount===0} type='button'>Add to Cart</Button>

            </ListGroup.Item>


            </ListGroup>
          </Card>
        </Col>

    </Row>

    </div>
    </Container>
  )
}

export default ProductScreen