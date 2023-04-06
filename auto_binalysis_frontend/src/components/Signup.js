import React, { useState } from "react";

import styles from "./css/Signup.module.css";
import { Card, Form } from "react-bootstrap";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Signup() {
  const [userData, setUserData] = useState({
    username: "",
    email: "",
    org_name: "",
    org_city: "",
    org_country: "",
    account_name: "",
    password: "",
    re_password: "",
    gender: "",
  });
  const navigate = useNavigate();

  const userTypeHandler = (event) => {
    console.log(event.target.value);
  };

  const changeHandler = (event) => {
    setUserData({ ...userData, [event.target.name]: event.target.value });
  };

  const submitHandler = async (event) => {
    console.log(userData);
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/auth/users/",
        userData
      );
      if (response.status === 201) {
        navigate("/login");
      }
    } catch (error) {
      console.log(Object.values(error?.response?.data)[0][0]);
    }
  };

  return (
    <Card className={styles.container}>
      <h1 className={styles.form_heading}>Sign Up</h1>
      <form onSubmit={submitHandler}>
        <div className={styles.inputs_container}>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            onChange={changeHandler}
            name="username"
            placeholder="Name"
          />
        </div>
        <div className={styles.inputs_container}>
          <label htmlFor="organizationName">Organization name</label>
          <input
            type="text"
            name="org_name"
            placeholder="Organization name"
            onChange={changeHandler}
          />
        </div>
        <div className={styles.inputs_container}>
          <label htmlFor="organizationCountry">Organization country</label>
          <input
            type="text"
            name="org_country"
            onChange={changeHandler}
            placeholder="Organization country"
          />
        </div>
        <div className={styles.inputs_container}>
          <label htmlFor="organizationCity">Organization city</label>
          <input
            type="text"
            name="org_city"
            placeholder="Organization city"
            onChange={changeHandler}
          />
        </div>
        <div className={styles.inputs_container}>
          <label htmlFor="accountName">Account name</label>
          <input
            type="text"
            name="account_name"
            placeholder="Account name"
            onChange={changeHandler}
          />
        </div>
        <div className={styles.inputs_container}>
          <label htmlFor="email">Email</label>
          <input
            type="text"
            onChange={changeHandler}
            name="email"
            placeholder="Email"
          />
        </div>
        <div className={styles.inputs_container}>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            onChange={changeHandler}
            name="password"
            placeholder="Password"
          />
        </div>
        <div className={styles.inputs_container}>
          <label htmlFor="cpassword">Confirm password</label>
          <input
            type="password"
            name="re_password"
            onChange={changeHandler}
            placeholder="Confirm password"
          />
        </div>
        <div className={styles.gender_container}>
          <div className={styles.gender_title}>
            <label>Gender</label>
          </div>
          <div className="radio_buttons_container">
            <input
              type="radio"
              name="gender"
              value="Male"
              style={{ marginLeft: "1rem" }}
            />
            <label htmlFor="Male" style={{ marginLeft: "10px" }}>
              Male
            </label>
            <input
              type="radio"
              name="gender"
              value="Female"
              style={{ marginLeft: "1rem" }}
            />
            <label htmlFor="Female" style={{ marginLeft: "10px" }}>
              Female
            </label>
          </div>
        </div>
        <div className={styles.market_select_container}>
          <Form.Select
            size="lg"
            aria-label="Default select example"
            onChange={userTypeHandler}
          >
            <option value="Local Super Market">Local Super Market</option>
            <option value="E-commerce Store">E-commerce Store</option>
          </Form.Select>
        </div>
        <button type="submit" className={styles.loginBtn}>
          Signup
        </button>
      </form>
    </Card>
  );
}

export default Signup;
