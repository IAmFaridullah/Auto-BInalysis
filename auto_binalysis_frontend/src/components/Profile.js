import React, { useState, useEffect } from "react";

import "./css/Profile.module.css";

import Card from "react-bootstrap/Card";
import profileImage from "../../src/assets/profile.png";
import { FaFacebookSquare } from "react-icons/fa";
import { AiFillInstagram } from "react-icons/ai";
import { FaWhatsappSquare } from "react-icons/fa";
import { BsYoutube } from "react-icons/bs";
import axios from "axios";

const Profile = () => {
  const [user, setUser] = useState({});
  const accessToken = window.localStorage.getItem("accessToken");

  // const user = JSON.parse(window.localStorage.getItem("user"));

  const getUserData = async () => {
    const response = await axios.get("http://localhost:8000/auth/users/me/", {
      headers: {
        Authorization: `JWT ${accessToken}`,
      },
    });
    console.log(response);
    setUser(response.data);
  };

  useEffect(() => {
    getUserData();
  }, []);

  return (
    <div className="profile_holder">
      <Card className="profile_container">
        <div className="profile_header">
          <Card className="image">
            <img src={profileImage} alt="profile visual identity" />
          </Card>
          <h6 className="title">{user?.name}</h6>
          <p className="subtitle">User</p>
        </div>
        <div className="social_profiles">
          <div className="social">
            <FaFacebookSquare className="icon" />
          </div>
          <div className="social">
            <AiFillInstagram
              className="icon"
              style={{ height: "2.3rem", width: "2.3rem" }}
            />
          </div>
          <div className="social">
            <FaWhatsappSquare className="icon" />
          </div>
          <div className="social">
            <BsYoutube
              className="icon"
              style={{ height: "2.7rem", width: "2.3rem" }}
            />
          </div>
        </div>
      </Card>
    </div>
  );
};

export default Profile;
