import React from 'react';
import { LinkContainer } from 'react-router-bootstrap';
import { Navbar, Nav, NavDropdown } from 'react-bootstrap';

function Header() {
  return (
    <>
      <Navbar expand="lg" bg="primary" variant="dark" className="navbar navbar-expand-lg">
        <div className="container-fluid">
          <LinkContainer to="/">
            <Navbar.Brand>STSmart</Navbar.Brand>
          </LinkContainer>

          <Navbar.Toggle aria-controls="navbarColor01" />
          <Navbar.Collapse id="navbarColor01">
            <Nav className="me-auto">
              <LinkContainer to="/">
                <Nav.Link className="navbar-link active">Home</Nav.Link>
              </LinkContainer>

              <LinkContainer to="/Pricing">
                <Nav.Link className="navbar-link active">Pricing</Nav.Link>
              </LinkContainer>

              <LinkContainer to="/About">
                <Nav.Link className="navbar-link active">About</Nav.Link>
              </LinkContainer>

              <NavDropdown title="Category" id="category-dropdown">
                <LinkContainer to="/category/dress">
                  <NavDropdown.Item>Dress</NavDropdown.Item>
                </LinkContainer>
                <LinkContainer to="/category/electronics">
                  <NavDropdown.Item>Electronics</NavDropdown.Item>
                </LinkContainer>
                <LinkContainer to="/category/accessories">
                  <NavDropdown.Item>Accessories</NavDropdown.Item>
                </LinkContainer>
                <LinkContainer to="/category/footwear">
                  <NavDropdown.Item>Foot Wear</NavDropdown.Item>
                </LinkContainer>
                <NavDropdown.Divider />
                <LinkContainer to="/category/offers">
                  <NavDropdown.Item>Offers</NavDropdown.Item>
                </LinkContainer>
              </NavDropdown>
            </Nav>

            <form className="d-flex">
              <input className="form-control me-sm-2" type="search" placeholder="Search" />
              <button className="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
            </form>

            <Nav className="ms-auto">
              <LinkContainer to="/cart">
                <Nav.Link><h5>🛒Cart</h5></Nav.Link>
              </LinkContainer>

              <NavDropdown title="Profile" id="profile-dropdown">
                <LinkContainer to="/profile/recommendations">
                  <NavDropdown.Item>Recommendations</NavDropdown.Item>
                </LinkContainer>
                <LinkContainer to="/profile/update">
                  <NavDropdown.Item>Update</NavDropdown.Item>
                </LinkContainer>
                <NavDropdown.Divider />
                <LinkContainer to="/logout">
                  <NavDropdown.Item>Logout</NavDropdown.Item>
                </LinkContainer>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </div>
      </Navbar>
    </>
  );
}

export default Header;
