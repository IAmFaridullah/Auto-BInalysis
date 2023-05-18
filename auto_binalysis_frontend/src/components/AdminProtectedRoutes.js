import { Navigate, Outlet } from "react-router-dom";

const AdminProtectedRoutes = () => {
  const loggedInUser = JSON.parse(window.localStorage.getItem("user"));
  return loggedInUser?.is_admin ? <Outlet /> : <Navigate to="/unauthorized" />;
};

export default AdminProtectedRoutes;
