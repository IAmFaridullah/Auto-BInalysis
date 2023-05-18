import React, { useState } from "react";

import styles from "./css/NewPassword.module.css";
import { Card } from "react-bootstrap";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function NewPassword() {
  const [userData, setUserData] = useState({
    new_password: "",
    re_new_password: "",
  });
  const navigate = useNavigate();
  const { uid, token } = useParams();

  const changeHandler = (event) => {
    setUserData({ ...userData, [event.target.name]: event.target.value });
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    const response = await axios.post(
      "http://localhost:8000/auth/users/reset_password_confirm/",
      {
        uid: uid,
        token: token,
        new_password: userData.new_password,
        re_new_password: userData.re_new_password,
      }
    );
    console.log(response);
    if (localStorage.getItem("accessToken")) {
      navigate("/profile");
    } else {
      navigate("/login");
    }
  };

  return (
    <>
      <div className={styles.container}>
        <h1 className={styles.form_heading}>Change password</h1>
        <form onSubmit={submitHandler}>
          <div className={styles.inputs_container}>
            <label htmlFor="password">New password</label>
            <input
              type="password"
              onChange={changeHandler}
              name="new_password"
            />
          </div>
          <div className={styles.inputs_container}>
            <label htmlFor="password">Confirm new password</label>
            <input
              type="password"
              onChange={changeHandler}
              name="re_new_repassword"
            />
          </div>
          <button type="submit" className={styles.loginBtn}>
            Change password
          </button>
        </form>
      </div>
    </>
  );
}

export default NewPassword;
