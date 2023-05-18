import React from "react";

import "./App.css";

import { Routes, Route, useLocation, Navigate } from "react-router-dom";
import Body from "./components/Body";
import Footer from "./components/Footer";
import Login from "./components/Login";
import Signup from "./components/Signup";
import ForgotPassword from "./components/ForgotPassword";
import NewPassword from "./components/NewPassword";
import Profile from "./components/Profile";
import Chatpage from "./components/chatpage/Chatpage";
import Navbar from "./components/Navbar";
import PopupChatbot from "./components/PopupChatbot";
import ChatContextProvider from "./components/context/chatcontext/Chatcontextprovider";
import AdminContextProvider from "./components/context/admincontext/Admincontextprovider";
import TrainedModels from "./components/Dashboard/TrainedModels";
import Dashboard from "./components/Dashboard/Dashboard";
import Home from "./components/HomePage/Home";
import ProtectedRoutes from "./components/ProtectedRoutes";
import Notfound from "./components/Notfound";
import TrainModel from "./components/TrainModel";
import TestModel from "./components/TestModel";
import AdminDashboard from "./components/AdminDashboard/AdminDashboard";
import UpdateUser from "./components/AdminDashboard/UpdateUser";
import UnAuthorized from "./components/UnAuthorized";
import AdminProtectedRoutes from "./components/AdminProtectedRoutes";

function App() {
  const location = useLocation();
  const isChatRoute = location.pathname.startsWith("/admin/chats");

  return (
    <div>
      {!isChatRoute && <Navbar />}
      {!isChatRoute && <PopupChatbot />}

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/reset-password" element={<ForgotPassword />} />
        <Route
          path="/password/reset/confirm/:uid/:token"
          element={<NewPassword />}
        />
        <Route path="/register" element={<Signup />} />
        <Route element={<ProtectedRoutes />}>
          <Route path="/profile" element={<Profile />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/models" element={<TrainedModels />} />
          <Route path="/train-model" element={<TrainModel />} />
          <Route path="/test-model/:name" element={<TestModel />} />
          <Route element={<AdminProtectedRoutes />}>
            <Route
              path="/admin/dashboard"
              element={
                <AdminContextProvider>
                  <AdminDashboard />
                </AdminContextProvider>
              }
            />
            <Route
              path="/admin/update-user/:username"
              element={
                <AdminContextProvider>
                  <UpdateUser />
                </AdminContextProvider>
              }
            />
            <Route
              path="/admin/chats/"
              element={
                <ChatContextProvider>
                  <Chatpage />
                </ChatContextProvider>
              }
            />
          </Route>
        </Route>

        <Route path="/unauthorized" element={<UnAuthorized />} />
        <Route path="*" element={<Notfound />} />
      </Routes>
      {!isChatRoute && <Footer />}
    </div>
  );
}

export default App;
