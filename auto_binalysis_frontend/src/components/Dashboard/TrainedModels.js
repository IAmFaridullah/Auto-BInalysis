import React from "react";

import { NavLink } from "react-router-dom";
import { BiRightArrowAlt } from "react-icons/bi";
import styles from "./TrainedModels.module.css";
import Model from "./Model";

function TrainedModels() {
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h3 className={styles.container_title}>Trained Models</h3>
        <NavLink to="/train-model">
          <div className={styles.train_model_btn}>
            Train model <BiRightArrowAlt className={styles.arrow_icon} />
          </div>
        </NavLink>
      </div>
      <div className={styles.models_container}>
        <Model />
        <Model />
        <Model />
        <Model />
        <Model />
        <Model />
        <Model />
        <Model />
      </div>
    </div>
  );
}

export default TrainedModels;
