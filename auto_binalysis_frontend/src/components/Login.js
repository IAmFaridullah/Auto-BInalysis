import React, { useState } from "react";

import styles from "./css/Login.module.css";
import { Card } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function Login() {
  const [userData, setUserData] = useState({
    email: "",
    password: "",
  });
  const navigate = useNavigate();

  const changeHandler = (event) => {
    setUserData({ ...userData, [event.target.name]: event.target.value });
  };

  const submitHandler = async (event) => {
    console.log(userData);
    event.preventDefault();
    const response = await axios.post(
      "http://localhost:8000/auth/jwt/create/",
      userData
    );
    if (response.status === 200) {
      window.localStorage.setItem("accessToken", response.data.access);
      window.localStorage.setItem("refreshToken", response.data.refresh);
      navigate("/profile");
    }
  };

  return (
    <Card className={styles.container}>
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
        <button type="submit" className={styles.loginBtn}>
          Login
        </button>
        <button className={styles.newAccountBtn}>Create new account</button>
      </form>
    </Card>
  );
}

export default Login;
