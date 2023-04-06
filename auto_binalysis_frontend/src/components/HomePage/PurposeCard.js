import React from "react";
import "./PurposeCard.css";

function PurposeCard(props) {
  return (
    <>
      <div className="card_container">
        <div className="card">
          <div className="card_data">
            <h3 className="title">Purpose</h3>
            <p className="desc">
              Business intelligence tools provide a powerful way to collect,
              transform, and analyze data from diverse sources, generating
              insights that can drive improvements in customer service,
              operations, and profitability. These tools can help organizations
              to better understand trends and patterns, identify areas of
              opportunity, and make informed decisions that support growth and
              success.
            </p>
          </div>
        </div>
      </div>
    </>
  );
}

export default PurposeCard;
