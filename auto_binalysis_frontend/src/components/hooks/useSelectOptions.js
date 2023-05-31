import React, { useContext } from "react";
import { visualizationContext } from "../context/visualizationcontext/VisualizationProvider";

function useSelectOptions() {
  const [state] = useContext(visualizationContext);
  const { model_name } = state;
  const {
    firstColumn,
    secondColumn,
    thirdColumn,
    fourthColumn,
    fifthColumn,
    sixthColumn,
    seventhColumn,
    eightColumn,
  } = state.data;

  if (model_name === "Member Card Analysis Data.pkl") {
    return {
      chart: {
        type: "pie", // Specify the chart type as a column
        marginRight: 10,
      },
      title: {
        text: "Member card analysis predictions", // Set the chart title
      },
      xAxis: {
        categories: ["YES", "NO"],
      },
      yAxis: {
        title: {
          text: "Value", // Set the y-axis title
        },
      },
      series: [
        {
          name: "Churn",
          data: [state.data.countYes, state.data.countNo], // Set the data for the vertical bars
        },
      ],
    };
  } else if (model_name === "PharmaSalesWeekly.pkl") {
    return {
      chart: {
        type: "line", // Specify the chart type as a line
        marginRight: 20,
      },
      title: {
        text: "Pharma Weekly Sales", // Set the chart title
      },
      yAxis: {
        title: {
          text: "Values", // Set the y-axis title
        },
      },
      series: [
        {
          name: "M01AB",
          data: firstColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 1
        },
        {
          name: "M01AE",
          data: secondColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "N02BA",
          data: thirdColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "N02BE",
          data: fourthColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "N05B",
          data: fifthColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "N05C",
          data: sixthColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "R03",
          data: seventhColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "R06",
          data: eightColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        // Add more series as needed
      ],
    };
  } else if (model_name === "Member Churn.pkl") {
    return {
      chart: {
        type: "pie",
        marginRight: 10, // Specify the chart type as a pie
      },
      title: {
        text: "Member Churn", // Set the chart title
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: "pointer",
          // colors: ["purple", "orange"], // Specify the slice colors

          dataLabels: {
            enabled: true,
            distance: -70, // Adjust this value to move the labels inside the slice
            format: "{point.percentage:.1f}%",
            style: {
              fontWeight: "bold",
              fontSize: "16px", // Adjust the font size here
              color: "white",
              textOutline: "none",
            },
          },
          showInLegend: true, // If you want to show a legend for the chart
        },
      },
      series: [
        {
          name: "Data",
          data: [
            ["YES", state.data.countYes], // Data for slice 1
            ["NO", state.data.countNo], // Data for slice 2
          ],
        },
      ],
    };
  } else if (model_name === "Monthly Sales Tableware.pkl") {
    return {
      chart: {
        type: "line", // Specify the chart type as a line
        marginRight: 20,
      },
      title: {
        text: "Tableware Monthly Sales", // Set the chart title
      },
      yAxis: {
        title: {
          text: "Values", // Set the y-axis title
        },
      },
      series: [
        {
          name: "Coffee & Tea",
          data: firstColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 1
        },
        {
          name: "Knives & Cutlery",
          data: secondColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        // Add more series as needed
      ],
    };
  } else if (model_name === "Rwp and Isb Customers Service data.pkl") {
    return {
      chart: {
        type: "column",
        marginRight: 20, // Specify the chart type as a column
      },
      title: {
        text: "Rawalpindi & Islamabad Customer Churn", // Set the chart title
      },
      xAxis: {
        categories: ["YES", "NO"], // Set the x-axis categories
      },
      yAxis: {
        title: {
          text: "Value", // Set the y-axis title
        },
      },
      series: [
        {
          name: "Churn",
          data: [state.data.countYes, state.data.countNo], // Set the data for the vertical bars
        },
      ],
    };
  } else if (model_name === "Daily Sales Toothpastes.pkl") {
    return {
      chart: {
        type: "line", // Specify the chart type as a line
      },
      title: {
        text: "Toothpastes Daily Sales", // Set the chart title
      },
      yAxis: {
        title: {
          text: "Values", // Set the y-axis title
        },
      },
      series: [
        {
          name: "Sensodyne",
          data: firstColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 1
        },
        {
          name: "Close Up",
          data: secondColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "Colgate",
          data: thirdColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "Dabur",
          data: fourthColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        // Add more series as needed
      ],
    };
  } else if (model_name === "Daily Orders Mob Acc.pkl") {
    return {
      chart: {
        type: "line", // Specify the chart type as a line
      },
      title: {
        text: "Mobile Accessories Daily Sales", // Set the chart title
      },
      yAxis: {
        title: {
          text: "Values", // Set the y-axis title
        },
      },
      series: [
        {
          name: "Mobile Covers",
          data: firstColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "Earphones",
          data: secondColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },
        {
          name: "Wireless Chargers",
          data: thirdColumn?.filter((value, index) => index !== 0 && value), // Set the data for series 2
        },

        // Add more series as needed
      ],
    };
  } else if (model_name === "Women's Clothing Reviews.pkl") {
    return {
      chart: {
        type: "column", // Specify the chart type as a column
      },
      title: {
        text: "Women's Clothing Reviews", // Set the chart title
      },
      xAxis: {
        categories: ["1 Star", "2 Star", "3 Star", "4 Star", "5 Star"], // Set the x-axis categories
      },
      yAxis: {
        title: {
          text: "Value", // Set the y-axis title
        },
      },
      series: [
        {
          name: "Churn",
          data: [
            state.data.oneRating,
            state.data.twoRating,
            state.data.threeRating,
            state.data.fourRating,
            state.data.fiveRating,
          ], // Set the data for the vertical bars
        },
      ],
    };
  }
}

export default useSelectOptions;
