import React from "react";
import { FaHome, FaUser } from "react-icons/fa";
import { IoMdAnalytics } from "react-icons/io";
import { useNavigate } from "react-router-dom";
import styles from "./Sidebar.module.css";

const Sidebar = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.sidebar}>
      <div className={styles.sidebar_item} onClick={() => navigate("/")}>
        <FaHome className={styles.sidebar_icon} />
        <span className={styles.sidebar_text}>Home</span>
      </div>
      <div className={styles.sidebar_item} onClick={() => navigate("/profile")}>
        <FaUser className={styles.sidebar_icon} />
        <span className={styles.sidebar_text}>Profile</span>
      </div>
      <div
        className={styles.sidebar_item}
        onClick={() => navigate("/train-model")}
      >
        <IoMdAnalytics className={styles.sidebar_icon} />
        <span className={styles.sidebar_text}>Train Model</span>
      </div>
    </div>
  );
};

export default Sidebar;
