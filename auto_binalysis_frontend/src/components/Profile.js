import React, { useState, useEffect } from "react";

import styles from "./css/Profile.module.css";

import profileImage from "../assets/profile.png";
import { FaFacebookSquare } from "react-icons/fa";
import { AiFillInstagram } from "react-icons/ai";
import { FaWhatsappSquare } from "react-icons/fa";
import { BsYoutube } from "react-icons/bs";
import axios from "axios";

const Profile = () => {
  const [message, setMessage] = useState("");
  const user = JSON.parse(window.localStorage.getItem("user"));

  const changePasswordHandler = async () => {
    const response = await axios.post(
      "http://localhost:8000/auth/users/reset_password/",
      { email: user?.email }
    );
    console.log(response);
  };

  return (
    <div className={styles.profile_holder}>
      <div className={styles.profile_container}>
        <div className={styles.profile_header}>
          <div className={styles.image}>
            <img src={profileImage} alt="profile visual identity" />
          </div>
          <h6 className={styles.title}>{user?.account_name}</h6>
          <p className={styles.subtitle}>{user?.email}</p>
          <p
            onClick={changePasswordHandler}
            className={styles.reset_password_link}
          >
            Change password
          </p>
        </div>
        <div className={styles.social_profiles}>
          <div className={styles.social}>
            <FaFacebookSquare className={styles.icon} />
          </div>
          <div className={styles.social}>
            <AiFillInstagram
              className={styles.icon}
              style={{ height: "2.3rem", width: "2.3rem" }}
            />
          </div>
          <div className={styles.social}>
            <FaWhatsappSquare className={styles.icon} />
          </div>
          <div className={styles.social}>
            <BsYoutube
              className={styles.icon}
              style={{ height: "2.7rem", width: "2.3rem" }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
