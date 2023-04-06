import React from "react";
import { useNavigate, NavLink } from "react-router-dom";
import "./css/Navbar.css";

import logo from "../images/Logo1.png";

const Navbar = () => {
  const navigate = useNavigate();
  const accessToken = localStorage.getItem("accessToken");

  const handleLogout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <img src={logo} alt="Logo" className="logo" />
      </div>
      <ul className="navbar-right">
        <li className="nav-item">
          <NavLink
            to="/"
            end
            // style={({ isActive }) =>
            //   isActive
            //     ? {
            //         backgroundColor: "orange",
            //         padding: "8px",
            //         borderRadius: "5px",
            //       }
            //     : null
            // }
          >
            Home
          </NavLink>
        </li>
        {accessToken && (
          <li className="nav-item">
            <NavLink
              to="/dashboard"
              // style={({ isActive }) =>
              //   isActive
              //     ? {
              //         backgroundColor: "orange",
              //         padding: "8px",
              //         borderRadius: "5px",
              //       }
              //     : null
              // }
            >
              Dashboard
            </NavLink>
          </li>
        )}
        {accessToken && (
          <li className="nav-item">
            <NavLink
              to="/profile"
              end
              // style={({ isActive }) =>
              //   isActive
              //     ? {
              //         backgroundColor: "orange",
              //         padding: "8px",
              //         borderRadius: "5px",
              //       }
              //     : null
              // }
            >
              Profile
            </NavLink>
          </li>
        )}
        {!accessToken && (
          <li className="nav_btn">
            <NavLink to="/login">Login</NavLink>
          </li>
        )}
        {!accessToken && (
          <li className="nav_btn">
            <NavLink to="/register">Register</NavLink>
          </li>
        )}
        {accessToken && (
          <li className="nav_btn logout_btn" onClick={handleLogout}>
            <NavLink>Logout</NavLink>
          </li>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
