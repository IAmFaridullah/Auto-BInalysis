import { useContext } from "react";

import * as XLSX from "xlsx";
import { visualizationContext } from "../context/visualizationcontext/VisualizationProvider";

const useExtractData = () => {
  const [state, dispatch] = useContext(visualizationContext);

  const handleExcelFile = (excelFile) => {
    const { model_name } = state;
    const reader = new FileReader();
    reader.onload = (e) => {
      const workbook = XLSX.read(e.target.result, { type: "binary" });
      const worksheet = workbook.Sheets[workbook.SheetNames[0]];
      const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
      if (model_name === "Member Card Analysis Data.pkl") {
        const xValues = jsonData.map((row) => row[7]);
        const countYes = xValues.filter((item) => item === "Yes").length;
        const countNo = xValues.filter((item) => item === "No").length;
        dispatch({
          type: "SET_DATA",
          payload: { countNo, countYes },
        });
      } else if (model_name == "PharmaSalesWeekly.pkl") {
        const datesColumn = jsonData.map((row) => row[0]);
        const firstColumn = jsonData.map((row) => row[1]);
        const secondColumn = jsonData.map((row) => row[2]);
        const thirdColumn = jsonData.map((row) => row[3]);
        const fourthColumn = jsonData.map((row) => row[4]);
        const fifthColumn = jsonData.map((row) => row[5]);
        const sixthColumn = jsonData.map((row) => row[6]);
        const seventhColumn = jsonData.map((row) => row[7]);
        const eightColumn = jsonData.map((row) => row[8]);
        dispatch({
          type: "SET_DATA",
          payload: {
            datesColumn,
            firstColumn,
            secondColumn,
            thirdColumn,
            fourthColumn,
            fifthColumn,
            sixthColumn,
            seventhColumn,
            eightColumn,
          },
        });
      } else if (model_name === "Member Churn.pkl") {
        const xValues = jsonData.map((row) => row[8]);
        const countYes = xValues.filter((item) => item === "Yes").length;
        const countNo = xValues.filter((item) => item === "No").length;
        dispatch({
          type: "SET_DATA",
          payload: { countNo, countYes },
        });
      } else if (model_name === "Monthly Sales Tableware.pkl") {
        const firstColumn = jsonData.map((row) => row[1]);
        const secondColumn = jsonData.map((row) => row[2]);
        dispatch({
          type: "SET_DATA",
          payload: { firstColumn, secondColumn },
        });
      } else if (model_name === "Rwp and Isb Customers Service data.pkl") {
        const xValues = jsonData.map((row) => row[9]);
        const countYes = xValues.filter((item) => item === "Yes").length;
        const countNo = xValues.filter((item) => item === "No").length;
        dispatch({
          type: "SET_DATA",
          payload: { countYes, countNo },
        });
      } else if (model_name === "Daily Sales Toothpastes.pkl") {
        const firstColumn = jsonData.map((row) => row[1]);
        const secondColumn = jsonData.map((row) => row[2]);
        const thirdColumn = jsonData.map((row) => row[3]);
        const fourthColumn = jsonData.map((row) => row[4]);
        dispatch({
          type: "SET_DATA",
          payload: { firstColumn, secondColumn, thirdColumn, fourthColumn },
        });
      } else if (model_name === "Daily Orders Mob Acc.pkl") {
        const firstColumn = jsonData.map((row) => row[1]);
        const secondColumn = jsonData.map((row) => row[2]);
        const thirdColumn = jsonData.map((row) => row[3]);
        dispatch({
          type: "SET_DATA",
          payload: { firstColumn, secondColumn, thirdColumn },
        });
      } else if (model_name === "Women's Clothing Reviews.pkl") {
        const ratingColumn = jsonData.map((row) => row[4]);
        const oneRating = ratingColumn.filter((item) => item === 1).length;
        const twoRating = ratingColumn.filter((item) => item === 2).length;
        const threeRating = ratingColumn.filter((item) => item === 3).length;
        const fourRating = ratingColumn.filter((item) => item === 4).length;
        const fiveRating = ratingColumn.filter((item) => item === 5).length;
        dispatch({
          type: "SET_DATA",
          payload: {
            oneRating,
            twoRating,
            threeRating,
            fourRating,
            fiveRating,
          },
        });
      } else {
        console.log("in else");
      }
    };

    reader.readAsBinaryString(excelFile);
  };

  return handleExcelFile;
};

export default useExtractData;
