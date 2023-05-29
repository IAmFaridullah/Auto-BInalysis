import React, { useContext } from "react";

import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";

import styles from "./css/Visualization.module.css";
import { visualizationContext } from "./context/visualizationcontext/VisualizationProvider";
import useSelectOptions from "./hooks/useSelectOptions";

require("highcharts/modules/exporting")(Highcharts);

function Visualization() {
  const chartOptions = useSelectOptions();
  return (
    <div className={styles.container}>
      <div>
        <HighchartsReact highcharts={Highcharts} options={chartOptions} />
      </div>
    </div>
  );
}

export default Visualization;
