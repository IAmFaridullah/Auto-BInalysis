import React from "react";
import "./Header.css";

import Bi from "../../assets/images/BI1.jpg";

const Header = () => {
  return (
    <div className="header-container">
      <div className="header-content">
        <div className="header-left">
          <h1 className="header-title">Auto Binalysis</h1>
          <h1 className="header-slogan">
            Remove barriers, find clarity, exceed goals
          </h1>
          <h2 className="header-sub-slogan">Lead your way to secure future</h2>
        </div>
        <div className="header-right">
          <img
            src={Bi}
            alt="Business intelligence tool"
            className="header-image"
          />
        </div>
      </div>
    </div>
  );
};

export default Header;
