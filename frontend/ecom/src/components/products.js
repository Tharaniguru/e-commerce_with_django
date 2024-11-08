import React from 'react'
import {Card, CardBody,} from 'react-bootstrap'
import Rating from './Rating'
import { Link } from 'react-router-dom'




function Products({product}) {
  return (
    <Card className='my-s p-3 rounded'>
        <Link to={`/product/${product._id}`}>
        
        <Card.Img src={product.image} /> 
        </Link>
        <CardBody>

        <Link to={`/product/${product._id}`} className='text-dark'>
        <Card.Title as="div">
            <strong>{product.productname}</strong>
        </Card.Title>
        </Link>

       

        <Card.Text as='h3'>
            Rs. {product.price}
        </Card.Text>

        <Card.Text>
            <div className='"my3'>
                {product.rating} reviews
            </div>
        </Card.Text>

        <Rating
               value={product.rating} 
               text={`${product.numReview} reviews`}
               color={"#f8e825"}
               />

        </CardBody>
    </Card>
  )
}

export default Products
