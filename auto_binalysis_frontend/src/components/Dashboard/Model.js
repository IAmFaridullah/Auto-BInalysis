import React from "react";

import { useNavigate } from "react-router-dom";
import styles from "./Model.module.css";

function Model({ name, accuracy }) {
  const navigate = useNavigate();
  const modelHandler = () => {
    navigate(`/test-model/${name}`);
  };

  return (
    <div className={styles.model} onClick={modelHandler}>
      <h5 className={styles.model_title}>{name}</h5>
      <div className={styles.model_accuracy_box}>
        <h6>Accuracy</h6>
        <h6>{accuracy}</h6>
      </div>
    </div>
  );
}

export default Model;
