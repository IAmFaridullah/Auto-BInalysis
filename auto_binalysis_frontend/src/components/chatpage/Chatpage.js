import React, { useEffect, useContext } from "react";
import Chat from "./Chat";

import styles from "./Chatpage.module.css";
import Sidebar from "./Sidebar";
import axios from "axios";
import { chatContext } from "../context/chatcontext/Chatcontextprovider";

function Chatpage() {
  const [, dispatch] = useContext(chatContext);
  const getUsers = async () => {
    const response = await axios.get("http://localhost:8000/chatbot/chats/");
    if (response.status === 200) {
      dispatch({
        type: "ADD_USERS",
        payload: response.data.users,
      });
    }
  };

  useEffect(() => {
    getUsers();
  }, []);

  return (
    <div className={styles.chatpage}>
      <Sidebar />
      <Chat />
    </div>
  );
}

export default Chatpage;
