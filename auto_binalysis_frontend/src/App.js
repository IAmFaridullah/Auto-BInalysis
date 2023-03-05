import "./App.css";

import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Body from "./components/Body";
import Footer from "./components/Footer";
import Login from "./components/Login";
import Signup from "./components/Signup";
import ForgotPassword from "./components/ForgotPassword";
import NewPassword from "./components/NewPassword";
import Profile from "./components/Profile";
import Chatbot from "./components/Chatbot";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Body />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/chatbot" element={<Chatbot />} />
        <Route path="/login" element={<Login />} />
        <Route path="/reset-password" element={<ForgotPassword />} />
        <Route
          path="/password/reset/confirm/:uid/:token"
          element={<NewPassword />}
        />
        <Route path="/register" element={<Signup />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
