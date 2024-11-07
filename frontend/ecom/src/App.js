import React from 'react';
import { Container } from 'react-bootstrap';
import Header from './components/Header';
import Footer from './components/Footer';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import HomeScreen from './components/screen/HomeScreen';
import SignupScreen from './components/screen/SignupScreen';
import LoginScreen from './components/screen/LoginScreen';
import CartScreen from './components/screen/CartScreen';
import Recommendation from './components/screen/Recommendation';
// import Product from './components/products';
import ProductScreen from './components/screen/ProductScreen';




function App() {
  return (
    <>
      <Router>
        <Header />
        <Container>
          <Routes>
            <Route exact path="/" element={<HomeScreen />} />
            <Route exact path="/login" element={<LoginScreen />} />
            <Route exact path="/signup" element={<SignupScreen />} />
            <Route exact path="/profile/recommendations" element={<Recommendation />} />
            <Route exact path="/cart" element={<CartScreen />} />
            <Route exact path="/product/:id" element={<ProductScreen />} />
            
          </Routes>
        </Container>
        <Footer />
      </Router>
    </>
  );
}

export default App;
