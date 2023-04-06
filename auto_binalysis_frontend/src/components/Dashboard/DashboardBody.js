import React from "react";

import styles from "./DashboardBody.module.css";
import TrainedModels from "./TrainedModels";

function DashboardBody() {
  return (
    <div className={styles.container}>
      <TrainedModels />
    </div>
  );
}

export default DashboardBody;
