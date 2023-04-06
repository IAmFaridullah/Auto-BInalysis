import React from "react";
import { FaHome, FaUser } from "react-icons/fa";
import { IoMdAnalytics } from "react-icons/io";
import styles from "./Sidebar.module.css";

const Sidebar = () => {
  return (
    <div className={styles.sidebar}>
      <div className={styles.sidebar_item}>
        <FaHome className={styles.sidebar_icon} />
        <span className={styles.sidebar_text}>Home</span>
      </div>
      <div className={styles.sidebar_item}>
        <FaUser className={styles.sidebar_icon} />
        <span className={styles.sidebar_text}>Profile</span>
      </div>
      <div className={styles.sidebar_item}>
        <IoMdAnalytics className={styles.sidebar_icon} />
        <span className={styles.sidebar_text}>Train Model</span>
      </div>
    </div>
  );
};

export default Sidebar;
