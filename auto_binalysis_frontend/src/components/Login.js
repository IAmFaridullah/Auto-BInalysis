import React, { useState } from "react";

import styles from "./css/Login.module.css";
import { Card } from "react-bootstrap";
import { useNavigate, Link } from "react-router-dom";
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
    event.preventDefault();
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
        <Link to="/reset-password" className={styles.forgot_text}>
          Forgot password?
        </Link>
        <button type="submit" className={styles.loginBtn}>
          Login
        </button>
        <button
          className={styles.newAccountBtn}
          onClick={() => navigate("/register")}
        >
          Create new account
        </button>
      </form>
    </Card>
  );
}

export default Login;
