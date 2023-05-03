import React, { useState, useRef, useEffect, useContext } from "react";

import styles from "./Chat.module.css";
import { IoSend } from "react-icons/io5";
import ChatBubble from "./ChatBubble";
import axios from "axios";
import profilePic from "../../assets/profile.png";
import { chatContext } from "../context/chatcontext/Chatcontextprovider";

function Chat() {
  const [chat, setChat] = useState();
  const [message, setMessage] = useState("");
  const messagesContainerRef = useRef();
  const [state] = useContext(chatContext);
  const [sending, setSending] = useState(false);
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
  }, [state.selectedUser, message]);

  useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop =
        messagesContainerRef.current.scrollHeight;
    }
  }, [chat, sending]);

  const changeHandler = (event) => {
    setMessage(event.target.value);
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    setSending(true);
    try {
      const response = await axios.post(
        "http://localhost:8000/chatbot/admin-chat/",
        { message: message, username: state.selectedUser.username }
      );
      setSending(false);
      if (response.status === 200) {
      }
      setMessage("");
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
      <div className={styles.messages_container} ref={messagesContainerRef}>
        {chat?.map((messageInfo, index) => (
          <ChatBubble
            key={index}
            message={messageInfo.message}
            isSender={messageInfo.sender === "iamadmin" ? true : false}
          />
        ))}
        {sending && <p style={{ textAlign: "center" }}>Sending message...</p>}
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
