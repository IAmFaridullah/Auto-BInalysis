import React from "react";

import styles from "./AdminDashboard.module.css";
import Sidebar from "../Dashboard/Sidebar";
import DashboardBody from "./DashboardBody";

function AdminDashboard() {
  return (
    <div className={styles.container}>
      <Sidebar />
      <DashboardBody />
    </div>
  );
}

export default AdminDashboard;
