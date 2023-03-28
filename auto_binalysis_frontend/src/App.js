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
import TrainedModels from "./components/TrainedModels";

function App() {
  const location = useLocation();
  const isChatRoute = location.pathname.startsWith("/chat");

  return (
    <div>
      {!isChatRoute && <Navbar />}
      {!isChatRoute && <PopupChatbot />}

      <Routes>
        <Route path="/" element={<Body />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/file-upload" element={<FileUpload />} />
        <Route path="/models" element={<TrainedModels />} />
        <Route
          path="/chat"
          element={
            <ChatContextProvider>
              <Chatpage />
            </ChatContextProvider>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/reset-password" element={<ForgotPassword />} />
        <Route
          path="/password/reset/confirm/:uid/:token"
          element={<NewPassword />}
        />
        <Route path="/register" element={<Signup />} />
      </Routes>
      {!isChatRoute && <Footer />}
    </div>
  );
}

export default App;
