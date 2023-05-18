import React, { useContext, useState } from "react";

import styles from "./UpdateUser.module.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";

import logo2 from "../../assets/images/Logo2.png";
import { Spinner } from "react-bootstrap";
import { AdminContext } from "../context/admincontext/Admincontextprovider";

function UpdateUser() {
  const [state] = useContext(AdminContext);
  const navigate = useNavigate();
  const { selectedUser } = state;
  const [userData, setUserData] = useState({
    username: selectedUser.username,
    email: selectedUser.email,
    name: selectedUser.name,
    city: selectedUser.city,
    country: selectedUser.country,
  });
  const [loading, setLoading] = useState(false);
  const changeHandler = (event) => {
    setUserData({ ...userData, [event.target.name]: event.target.value });
  };

  const updateUserHandler = async (event, username) => {
    event.preventDefault();
    setLoading(true);
    const response = await axios.post(
      "http://localhost:8000/adminpanel/update-user/",
      {
        username: username,
        userData: userData,
      }
    );
    if (response.status === 200) {
      setLoading(false);
      navigate("/admin/dashboard");
    }
  };
  return (
    <div className={styles.container}>
      <div className={styles.logo}>
        <img src={logo2} alt="" />
      </div>
      <div className={styles.form_container}>
        <h4 className={styles.form_heading}>Update user</h4>
        <form onSubmit={updateUserHandler}>
          <div className={styles.inputs_container}>
            <label htmlFor="email">Username</label>
            <input
              type="text"
              onChange={changeHandler}
              name="username"
              defaultValue={state.selectedUser.username}
            />
          </div>
          <div className={styles.inputs_container}>
            <label htmlFor="email">Email</label>
            <input
              type="email"
              onChange={changeHandler}
              name="email"
              defaultValue={state.selectedUser.email}
            />
          </div>
          <div className={styles.inputs_container}>
            <label htmlFor="account_name">Name</label>
            <input
              type="text"
              onChange={changeHandler}
              name="name"
              defaultValue={state.selectedUser.name}
            />
          </div>
          <div className={styles.inputs_container}>
            <label htmlFor="city">City</label>
            <input
              type="text"
              onChange={changeHandler}
              name="city"
              defaultValue={state.selectedUser.city}
            />
          </div>
          <div className={styles.inputs_container}>
            <label htmlFor="country">Country</label>
            <input
              type="text"
              onChange={changeHandler}
              name="country"
              defaultValue={state.selectedUser.country}
            />
          </div>
          <button type="submit" className={styles.loginBtn}>
            {loading ? <Spinner /> : "Update"}
          </button>
        </form>
      </div>
    </div>
  );
}

export default UpdateUser;
