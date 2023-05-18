import React from "react";
import { FaHome, FaUser } from "react-icons/fa";
import { BsFillChatDotsFill } from "react-icons/bs";
import { useNavigate } from "react-router-dom";
import styles from "./AdminSidebar.module.css";

const AdminSidebar = () => {
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
        onClick={() => navigate("/admin/chats")}
      >
        <BsFillChatDotsFill className={styles.sidebar_icon} />
        <span className={styles.sidebar_text}>Chat</span>
      </div>
    </div>
  );
};

export default AdminSidebar;
