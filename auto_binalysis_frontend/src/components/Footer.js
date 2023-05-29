import React from "react";
import facebook from "../assets/images/facebook.png";
import twitter from "../assets/images/twitter.png";
import instagram from "../assets/images/instagram.png";
import phone from "../images/telephone.png";
import youtube from "../assets/images/youtube.png";
import linkedin from "../assets/images/linkedin.png";
import whatsapp from "../assets/images/whatsapp.png";
import gmail from "../assets/images/gmail.png";
import "./css/Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer__item">
        <h3>Business Intelligence Tool</h3>
        <p>
          Business intelligence tools provide a powerful way to collect,
          transform, and analyze data from diverse sources, generating insights
          that can drive improvements in customer service, operations, and
          profitability.
        </p>
      </div>
      <div className="footer__item">
        <h3>Contact Us</h3>
        <ul className="contact_section">
          <li>
            <img src={gmail} alt=""></img>
            <span> autobi45@gmail.com</span>
          </li>
          <li>
            <img src={phone} alt=""></img>
            <span> +051 123 456 789</span>
          </li>
          <li>
            <img src={whatsapp} alt=""></img>
            <span> +92 3123456789</span>
          </li>
        </ul>
      </div>
      <div className="footer__item ">
        <h3>Connect With Us</h3>
        <ul className="social_section">
          <li>
            <a href="https://www.linkedin.com">
              <img src={linkedin} alt="linkedin" />
            </a>
          </li>
          <li>
            <a href="https://www.youtube.com">
              <img src={youtube} alt="youtube" />
            </a>
          </li>
          <li>
            <a href="https://www.facebook.com">
              <img src={facebook} alt="facebook" />
            </a>
          </li>
          <li>
            <a href="https://www.twitter.com">
              <img src={twitter} alt="twitter" />
            </a>
          </li>
          <li>
            <a href="https://www.instagram.com">
              <img src={instagram} alt="instagram" />
            </a>
          </li>
        </ul>
      </div>
    </footer>
  );
}

export default Footer;
