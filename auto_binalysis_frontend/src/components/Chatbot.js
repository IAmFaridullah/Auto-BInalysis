import React, { useState } from "react";

import styles from "./css/Chatbot.module.css";
import { Card, Alert } from "react-bootstrap";
import axios from "axios";

function Chatbot() {
  const [question, setQuestion] = useState({
    question: "",
  });
  const [answers, setAnswers] = useState([]);

  const changeHandler = (event) => {
    setQuestion({ ...question, [event.target.name]: event.target.value });
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    const response = await axios.post(
      "http://localhost:8000/chatbot/response/",
      question
    );
    setAnswers([...answers, response.data.answer]);
    setQuestion(() => {
      setQuestion({ question: "" });
    });
  };

  return (
    <>
      <Card className={styles.container}>
        <h1 className={styles.form_heading}>Chatbot</h1>
        <form onSubmit={submitHandler}>
          <div className={styles.inputs_container}>
            <label htmlFor="question">Question</label>
            <input
              type="text"
              onChange={changeHandler}
              name="question"
              value={question?.question}
            />
          </div>
          <button type="submit" className={styles.loginBtn}>
            Ask
          </button>
        </form>
        {answers.map((answer, index) => (
          <Alert key={index} variant="primary" style={{ marginTop: "6px" }}>
            {answer}
          </Alert>
        ))}
      </Card>
    </>
  );
}

export default Chatbot;
