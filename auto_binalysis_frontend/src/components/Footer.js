import React from "react";
import gmail from "../images/gmail.png";
import phone from "../images/telephone.png";
import whatsapp from "../images/whatsapp.png";
import youtube from "../images/youtube.png";
import twitter from "../images/twitter.png";
import instagram from "../images/instagram.png";
import linkedin from "../images/linkedin.png";
import facebook from "../images/facebook.png";
import "./css/Footer.css";

export default function Footer() {
  return (
    <div className="footer">
      <div className="row row-footer" style={{ width: "%", margin: "auto" }}>
        <div className="col-sm-12 col-md-3">
          <ul>
            <li>
              <h2>Auto-BInalysis</h2>
            </li>
            <li>
              <p>An artifical intelligence tools to analyze data</p>
            </li>
          </ul>
        </div>

        <div className="col-sm-12 col-md-6 col-lg-3">
          <ul>
            <li>
              <h2>About Us</h2>
            </li>
            <li>
              <p>
                There is nothing about us, its our fyp and dont know if it get
                completes on time :P
              </p>
            </li>
          </ul>
        </div>
        <div className="col-sm-12 col-md-6 col-lg-3">
          <>
            <ul>
              <li>
                <h2>Contacts</h2>
              </li>
              <li>
                <img src={gmail} alt=""></img>
                <span> auto_binalysis@gmail.com</span>
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
          </>
        </div>
        <div className="col-sm-12 col-md-6 col-lg-3">
          <>
            <ul>
              <li>
                <h2>Social Media</h2>
              </li>
              <li>
                <img src={facebook} alt=""></img>
                <span> Facebook</span>
              </li>
              <li>
                <img src={instagram} alt=""></img>
                <span> Instagram</span>
              </li>
              <li>
                <img src={linkedin} alt=""></img> <span> Linkedin</span>
              </li>
              <li>
                <img src={twitter} alt=""></img>
                <span> Twitter</span>
              </li>
              <li>
                <img src={youtube} alt=""></img>
                <span> Youtube</span>
              </li>
            </ul>
          </>
        </div>
      </div>
    </div>
  );
}
