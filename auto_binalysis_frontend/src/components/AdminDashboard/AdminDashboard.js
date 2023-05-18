import React from "react";

import styles from "./AdminDashboard.module.css";
import AdminSidebar from "./AdminSidebar";
import DashboardBody from "./DashboardBody";

function AdminDashboard() {
  return (
    <div className={styles.container}>
      <AdminSidebar />
      <DashboardBody />
    </div>
  );
}

export default AdminDashboard;
