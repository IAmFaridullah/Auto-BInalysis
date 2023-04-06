import React from "react";

import { useNavigate } from "react-router-dom";
import styles from "./Model.module.css";

function Model({ model }) {
  const navigate = useNavigate();
  const modelHandler = () => {
    navigate(`/test-model/${model.model_name}`);
  };

  const selectRightElement = () => {
    if (model.accuracy !== null) {
      return (
        <div className={styles.model_accuracy_box}>
          <h6>Accuracy</h6>
          <h6>{model.accuracy}</h6>
        </div>
      );
    } else if (model.rmse !== null) {
      return (
        <div className={styles.model_accuracy_box}>
          <h6>Rmse</h6>
          <h6>{model.rmse}</h6>
        </div>
      );
    } else if (model.silhouette !== null) {
      return (
        <div className={styles.model_accuracy_box}>
          <h6>Silhouette</h6>
          <h6>{model.silhouette}</h6>
        </div>
      );
    } else {
      return null;
    }
  };

  return (
    <div className={styles.model} onClick={modelHandler}>
      <h5 className={styles.model_title}>{model.model_name}</h5>
      {selectRightElement()}
    </div>
  );
}

export default Model;
