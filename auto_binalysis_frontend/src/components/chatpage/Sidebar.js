import React, { useContext } from "react";

import styles from "./Sidebar.module.css";
import SidebarUser from "./SidebarUser";
import { chatContext } from "../context/chatcontext/Chatcontextprovider";

function Sidebar() {
  const [state] = useContext(chatContext);

  return (
    <div className={styles.sidebar}>
      <div className={styles.sidebar_header}>
        <div className={styles.profile_pic}></div>
      </div>
      <div className={styles.sidebar_body}>
        {state.users?.map((user, index) => (
          <SidebarUser key={index} user={user} />
        ))}
      </div>
    </div>
  );
}

export default Sidebar;
