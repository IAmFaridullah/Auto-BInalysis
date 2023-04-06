import React from "react";
import styles from "./CardSection.module.css";

import ecommerce from "../../assets/images/ecommerce.jpg";
import superstore from "../../assets/images/superstore.jpg";

const CardSection = () => {
  return (
    <section className={styles.card_section}>
      <div className={styles.card}>
        <div className={styles.image}>
          <img src={ecommerce} alt="Card 1" />
        </div>
        <div className={styles.desc}>
          <h2>E-commerece</h2>
          <ul>
            <li> Data Acquisition</li>
            <li> Data Mining</li>
            <li> Data Preprocessing</li>
            <li> Data Visualization</li>
            <li> Customer Churn Prediction</li>
            <li> Product Grouping</li>
            <li> Sales Analysis</li>
            <li> Sales Predictions</li>
            <li> Reporting</li>
          </ul>
        </div>
      </div>
      <div className={styles.card}>
        <div className={styles.image}>
          <img src={superstore} alt="Card 2" />
        </div>
        <div className={styles.desc}>
          <h2>Super store</h2>
          <ul>
            <li> Data Acquisition</li>
            <li> Data Mining</li>
            <li> Data Preprocessing</li>
            <li> Data Visualization</li>
            <li> Customer Churn Prediction</li>
            <li> Product Grouping</li>
            <li> Sales Analysis</li>
            <li> Sales Predictions</li>
            <li> Reporting</li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default CardSection;
