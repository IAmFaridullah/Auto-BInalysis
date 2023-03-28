import React, { useState, useRef, useEffect, useContext } from "react";

import styles from "./Chat.module.css";
import { IoSend } from "react-icons/io5";
import Message from "../Message";
import axios from "axios";
import profilePic from "../../assets/profile.png";
import { chatContext } from "../context/chatcontext/Chatcontextprovider";

function Chat() {
  const [chat, setChat] = useState();
  const [message, setMessage] = useState("");
  const messagesContainerRef = useRef();
  const [state, dispatch] = useContext(chatContext);

  const getUserChat = async () => {
    const response = await axios.post(
      "http://localhost:8000/chatbot/user-chats/",
      {
        username: state.selectedUser.username,
      }
    );
    if (response.status === 200) {
      setChat(response.data.user_chats);
    }
  };

  useEffect(() => {
    getUserChat();
  }, [state.selectedUser]);

  const changeHandler = (event) => {
    setMessage(event.target.value);
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/chatbot/admin-chat/",
        { message: message }
      );
      if (response.status === 200) {
        console.log("message sent successfully");
      }
    } catch (err) {
      if (err) {
        console.log(err);
      }
    }
  };
  return (
    <div className={styles.chat}>
      <div className={styles.chat_header}>
        <div className={styles.profile_pic}>
          <img src={profilePic} alt="profile pic" />
        </div>
        <p className={styles.profile_name}> {state.selectedUser?.name}</p>
      </div>
      <div className={styles.messages_container}>
        {chat?.map((messageInfo, index) => (
          <Message
            key={index}
            message={messageInfo.message}
            isSender={messageInfo.isSender}
          />
        ))}
      </div>
      <div className={styles.chat_input_container}>
        <form onSubmit={submitHandler}>
          <div className={styles.chat_input}>
            <input
              type="text"
              onChange={changeHandler}
              name="question"
              value={message}
              placeholder="Type your message..."
            />
            <button hidden type="submit" className={styles.send_icon} />
            <div className={styles.send_icon} onClick={submitHandler}>
              <IoSend />
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Chat;
