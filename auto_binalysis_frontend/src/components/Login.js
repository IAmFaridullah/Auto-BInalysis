import React, { useState } from "react";

import styles from "./css/Login.module.css";
import logo2 from "../assets/images/Logo2.png";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import { Spinner } from "react-bootstrap";

function Login() {
  const [userData, setUserData] = useState({
    email: "",
    password: "",
  });
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const changeHandler = (event) => {
    setUserData({ ...userData, [event.target.name]: event.target.value });
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post(
        "http://localhost:8000/auth/jwt/create/",
        userData
      );
      if (response.status === 200) {
        const resp = await axios.get("http://localhost:8000/auth/users/me/", {
          headers: {
            Authorization: `JWT ${response.data.access}`,
          },
        });
        localStorage.setItem("user", JSON.stringify(resp.data));
        localStorage.setItem("accessToken", response.data.access);
        localStorage.setItem("refreshToken", response.data.refresh);
        setLoading(false);
        if (resp.data.is_admin === true) {
          navigate("/profile");
        } else {
          navigate("/dashboard");
        }
      }
    } catch (error) {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.logo}>
        <img src={logo2} alt="" />
      </div>
      <div className={styles.form_container}>
        <h1 className={styles.form_heading}>Sign In</h1>
        <form onSubmit={submitHandler}>
          <div className={styles.inputs_container}>
            <label htmlFor="email">Email</label>
            <input type="email" onChange={changeHandler} name="email" />
          </div>
          <div className={styles.inputs_container}>
            <label htmlFor="password">Password</label>
            <input type="password" onChange={changeHandler} name="password" />
          </div>
          <Link to="/reset-password" className={styles.forgot_text}>
            Forgot password?
          </Link>
          <button type="submit" className={styles.loginBtn}>
            {loading ? <Spinner /> : "Login"}{" "}
          </button>
          <button
            className={styles.newAccountBtn}
            onClick={() => navigate("/register")}
          >
            Create new account
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;
