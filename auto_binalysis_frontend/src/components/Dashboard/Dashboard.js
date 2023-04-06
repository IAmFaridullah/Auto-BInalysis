import React from "react";
import Sidebar from "./Sidebar";

import styles from "./Dashboard.module.css";
import DashboardBody from "./DashboardBody";

function Dashboard() {
  return (
    <div className={styles.container}>
      <Sidebar />
      <DashboardBody />
    </div>
  );
}

export default Dashboard;
