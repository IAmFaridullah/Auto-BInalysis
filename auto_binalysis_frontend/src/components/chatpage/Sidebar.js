import React, { useContext } from "react";

import styles from "./Sidebar.module.css";
import SidebarUser from "./SidebarUser";
import { chatContext } from "../context/chatcontext/Chatcontextprovider";

function Sidebar() {
  const [state] = useContext(chatContext);
  const loggedInUser = JSON.parse(window.localStorage.getItem("user"));
  const [firstName, lastName] =
    loggedInUser && loggedInUser.account_name.split(" ");

  return (
    <div className={styles.sidebar}>
      <div className={styles.sidebar_header}>
        <div className={styles.profile_pic}>
          <span className={styles.profile_label}>
            {firstName[0]?.charAt(0).toUpperCase()}
            {lastName[0]?.charAt(0).toUpperCase()}
          </span>
        </div>
      </div>
      <div className={styles.sidebar_body}>
        {state.chatUsers?.map((user, index) => (
          <SidebarUser key={index} user={user} />
        ))}
      </div>
    </div>
  );
}

export default Sidebar;
