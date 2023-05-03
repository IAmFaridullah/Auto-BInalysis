import React from "react";

import styles from "./ChatBubble.module.css";

const Message = ({ message, isSender }) => {
  return (
    <div className={isSender ? styles.sender : styles.reciever}>{message}</div>
  );
};

export default Message;
