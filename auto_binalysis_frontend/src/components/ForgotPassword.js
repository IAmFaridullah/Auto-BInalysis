import React, { useState } from "react";
import styles from "./css/ForgotPassword.module.css";
import { Card } from "react-bootstrap";
import axios from "axios";

function ForgotPassword() {
  const [userData, setUserData] = useState({ email: "" });
  const changeHandler = (event) => {
    setUserData({ ...userData, email: event.target.value });
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    const response = await axios.post(
      "http://localhost:8000/auth/users/reset_password/",
      userData
    );
    console.log(response);
  };

  return (
    <>
      <Card className={styles.container}>
        <h1 className={styles.form_heading}>Reset password</h1>
        <form onSubmit={submitHandler}>
          <div className={styles.inputs_container}>
            <label htmlFor="email">Email</label>
            <input type="email" onChange={changeHandler} name="email" />
          </div>
          <button type="submit" className={styles.loginBtn}>
            Send recovery link
          </button>
        </form>
      </Card>
    </>
  );
}

export default ForgotPassword;
