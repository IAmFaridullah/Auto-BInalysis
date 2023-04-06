import React from "react";

import "./App.css";

import { Routes, Route, useLocation } from "react-router-dom";
import Body from "./components/Body";
import Footer from "./components/Footer";
import Login from "./components/Login";
import Signup from "./components/Signup";
import ForgotPassword from "./components/ForgotPassword";
import NewPassword from "./components/NewPassword";
import Profile from "./components/Profile";
import FileUpload from "./components/FileUpload";
import Chatpage from "./components/chatpage/Chatpage";
import Navbar from "./components/Navbar";
import PopupChatbot from "./components/PopupChatbot";
import ChatContextProvider from "./components/context/chatcontext/Chatcontextprovider";
import TrainedModels from "./components/Dashboard/TrainedModels";
import Dashboard from "./components/Dashboard/Dashboard";
import Home from "./components/HomePage/Home";
import ProtectedRoutes from "./components/ProtectedRoutes";
import Notfound from "./components/Notfound";

function App() {
  const location = useLocation();
  const isChatRoute = location.pathname.startsWith("/chat");

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
          <Route
            path="/train-model"
            element={
              <FileUpload url="http://localhost:8000/analysis/train-model/" />
            }
          />
          <Route
            path="/test-model"
            element={
              <FileUpload url="http://localhost:8000/analysis/test-model/" />
            }
          />
          <Route
            path="/chat"
            element={
              <ChatContextProvider>
                <Chatpage />
              </ChatContextProvider>
            }
          />
        </Route>

        <Route path="*" element={<Notfound />} />
      </Routes>
      {!isChatRoute && <Footer />}
    </div>
  );
}

export default App;
