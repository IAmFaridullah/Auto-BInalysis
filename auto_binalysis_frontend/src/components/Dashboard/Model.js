import React from "react";

import styles from "./Model.module.css";

function Model() {
  return (
    <div className={styles.model}>
      <h5 className={styles.model_title}>Churn Svm</h5>
      <div className={styles.model_accuracy_box}>
        <h6>Accuracy</h6>
        <h6>90%</h6>
      </div>
    </div>
  );
}

export default Model;
