import React from "react";
import logo from "../images/Logo1.png";
import "./css/Navbar.css";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();
  return (
    <div className="container" style={{ maxWidth: "100%", padding: "0%" }}>
      <nav className="navbar navbar-expand-lg">
        <div className="container-fluid">
          <img src={logo} id="logo" alt="" />

          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <a className="nav-link" href="/">
                  Home
                </a>
              </li>
              <li className="nav-item ">
                <a className="nav-link " href="/">
                  Services
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/">
                  About
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/">
                  Contact
                </a>
              </li>
            </ul>
          </div>
          <button
            type="button"
            // id="login"
            className="btn btn-danger"
            style={{ marginRight: "1rem" }}
            onClick={() => {
              localStorage.clear();
              navigate("/login");
            }}
          >
            Logout
          </button>
          <button
            type="button"
            // id="login"
            className="btn btn-success"
            onClick={() => {
              navigate("/login");
            }}
          >
            Login
          </button>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
        </div>
      </nav>
    </div>
  );
}
