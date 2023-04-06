import React, { useEffect, useState } from "react";

import { NavLink } from "react-router-dom";
import { BiRightArrowAlt } from "react-icons/bi";
import styles from "./TrainedModels.module.css";
import Model from "./Model";
import axios from "axios";

function TrainedModels() {
  const [models, setModels] = useState([]);
  const user = JSON.parse(window.localStorage.getItem("user"));

  const getUserModels = async () => {
    const response = await axios.post(
      "http://localhost:8000/analysis/user-models/",
      {
        username: user.username,
      }
    );
    if (response.status === 200) {
      console.log(response.data);
      setModels(response.data.models_data);
    }
  };
  useEffect(() => {
    getUserModels();
  }, []);
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
        {models.map((model) => (
          <Model model={model} />
        ))}
      </div>
    </div>
  );
}

export default TrainedModels;
