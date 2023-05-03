import React, { useEffect, useContext, useCallback } from "react";
import Chat from "./Chat";

import styles from "./Chatpage.module.css";
import Sidebar from "./Sidebar";
import axios from "axios";
import { chatContext } from "../context/chatcontext/Chatcontextprovider";

function Chatpage() {
  const [, dispatch] = useContext(chatContext);
  const getUsers = useCallback(async () => {
    const response = await axios.get("http://localhost:8000/chatbot/chats/");
    if (response.status === 200) {
      dispatch({
        type: "ADD_CHAT_USERS",
        payload: response.data.users,
      });
      dispatch({
        type: "SELECT_USER",
        payload: response.data.users[0],
      });
    }
  }, [dispatch]);

  useEffect(() => {
    getUsers();
  }, [getUsers]);

  return (
    <div className={styles.chatpage}>
      <Sidebar />
      <Chat />
    </div>
  );
}

export default Chatpage;
