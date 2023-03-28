import React, { useEffect, useRef, useState } from "react";
import axios from "axios";

import styles from "./css/PopupChatbot.module.css";
import { MdOutlineClose } from "react-icons/md";
import { IoSend } from "react-icons/io5";
import { BsFillChatDotsFill } from "react-icons/bs";

import Message from "./Message";

function PopupChatbot() {
  const [question, setQuestion] = useState("");
  const [chat, setChat] = useState([
    {
      messageText: "Hi, welcome to AutoBinalysis. How may i help you?",
      isSender: false,
    },
  ]);
  const [showChatBot, setShowChatBot] = useState(false);
  const chatContainerRef = useRef();

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [chat, showChatBot]);

  const chatBotToggler = () => {
    setShowChatBot(!showChatBot);
  };

  const changeHandler = (event) => {
    setQuestion(event.target.value);
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    if (question) {
      setChat([...chat, { messageText: question, isSender: true }]);
      const response = await axios.post(
        "http://localhost:8000/chatbot/response/",
        {
          question: question,
        }
      );
      if (response.status === 200) {
        setChat((prevState) => {
          return [
            ...prevState,
            { messageText: response.data.answer, isSender: false },
          ];
        });
      }

      setQuestion("");
    }
  };

  return (
    <>
      <div className={styles.toggler} onClick={chatBotToggler}>
        <BsFillChatDotsFill className={styles.toggler_icon} />
      </div>
      {showChatBot && (
        <div
          className={`${styles.chatbot} ${showChatBot ? styles.show : null}`}
        >
          <div className={styles.chatbot_header}>
            <div className={styles.chatbot_title}>Chatbot</div>
            <div className={styles.chatbot_close} onClick={chatBotToggler}>
              <MdOutlineClose />
            </div>
          </div>
          <div className={styles.chatbot_body} ref={chatContainerRef}>
            {chat?.map((message, index) => (
              <Message
                key={index}
                message={message.messageText}
                isSender={message.isSender}
              />
            ))}
          </div>
          <div className={styles.chatbot_input_container}>
            <form onSubmit={submitHandler}>
              <div className={styles.chatbot_input}>
                <input
                  type="text"
                  onChange={changeHandler}
                  name="question"
                  value={question}
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
      )}
    </>
  );
}

export default PopupChatbot;
