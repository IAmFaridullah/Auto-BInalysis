import React from "react";

import styles from "./css/TrainedModels.module.css";

function TrainedModels() {
  return (
    <div className={styles.container}>
      <div className={styles.models_container}>
        <div className={styles.model}>
          <h5 className={styles.model_title}>Churn Svm</h5>
          <div className={styles.model_accuracy_box}>
            <h6>Accuracy</h6>
            <h6>90%</h6>
          </div>
        </div>
        <div className={styles.model}>
          <h5 className={styles.model_title}>Churn Svm</h5>
          <div className={styles.model_accuracy_box}>
            <h6>Accuracy</h6>
            <h6>90%</h6>
          </div>
        </div>
        <div className={styles.model}>
          <h5 className={styles.model_title}>Churn Svm</h5>
          <div className={styles.model_accuracy_box}>
            <h6>Accuracy</h6>
            <h6>90%</h6>
          </div>
        </div>
        <div className={styles.model}>
          <h5 className={styles.model_title}>Churn Svm</h5>
          <div className={styles.model_accuracy_box}>
            <h6>Accuracy</h6>
            <h6>90%</h6>
          </div>
        </div>
        <div className={styles.model}>
          <h5 className={styles.model_title}>Churn Svm</h5>
          <div className={styles.model_accuracy_box}>
            <h6>Accuracy</h6>
            <h6>90%</h6>
          </div>
        </div>
        <div className={styles.model}>
          <h5 className={styles.model_title}>Churn Svm</h5>
          <div className={styles.model_accuracy_box}>
            <h6>Accuracy</h6>
            <h6>90%</h6>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TrainedModels;
