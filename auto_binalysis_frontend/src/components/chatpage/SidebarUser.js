import React, { useContext } from "react";
import { chatContext } from "../context/chatcontext/Chatcontextprovider";

import styles from "./SidebarUser.module.css";

function SidebarUser({ user }) {
  const [firstName, lastName] = user.name.split(" ");
  const [, dispatch] = useContext(chatContext);

  const selectUserHandler = (selectedUser) => {
    dispatch({
      type: "SELECT_USER",
      payload: selectedUser,
    });
  };

  return (
    <div
      className={styles.sidebar_user}
      onClick={() => selectUserHandler(user)}
    >
      <div className={styles.profile_pic}>
        <span className={styles.profile_label}>
          {firstName[0].charAt(0)}
          {lastName[0].charAt(0)}
        </span>
      </div>
      <div className={styles.profile_info}>
        <p className={styles.profile_name}>{user.name}</p>
        <p className={styles.profile_email}>{user.email}</p>
      </div>
    </div>
  );
}

export default SidebarUser;
