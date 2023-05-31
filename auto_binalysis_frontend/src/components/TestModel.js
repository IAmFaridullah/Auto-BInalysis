import axios from "axios";
import styles from "./css/TestModel.module.css";
import React, { useState, useCallback, useContext } from "react";
import { useDropzone } from "react-dropzone";
import { MdCloudUpload } from "react-icons/md";
import { useParams, useNavigate } from "react-router-dom";
import useExtractData from "./hooks/useExtractData";
import { visualizationContext } from "./context/visualizationcontext/VisualizationProvider";
import { centerImage } from "highcharts";
// import { FileSaver } from "file-saver";

function TestModel() {
  const [files, setFiles] = useState([]);
  const user = JSON.parse(localStorage.getItem("user"));
  const { name } = useParams();
  const navigate = useNavigate();
  const [, dispatch] = useContext(visualizationContext);
  const handleExcelFile = useExtractData();

  const onDrop = useCallback((acceptedFiles) => {
    dispatch({
      type: "SET_MODEL_NAME",
      payload: name,
    });
    setFiles(files.concat(acceptedFiles));
    // Do something with the files
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  const fileSubmitHandler = async () => {
    const formData = new FormData();
    formData.append("file", files[0]);
    formData.append("username", user.username);
    formData.append("model_name", name);
    axios
      .post("http://localhost:8000/analysis/test-model/", formData, {
        responseType: "blob",
      })
      .then((response) => {
        if (response.status === 200) {
          handleExcelFile(response.data);
          var FileSaver = require("file-saver");
          var blob = new Blob([response.data], {
            type: "application/ms-excel",
          });
          FileSaver.saveAs(blob, "predictions.xlsx");
          navigate("/test-model/visualization");
        }
      });
  };

  return (
    <div className={styles.dropzone_container}>
      <h2>Upload Testing Dataset</h2>
      <div {...getRootProps()} className={styles.dropzone}>
        <input {...getInputProps()} />
        {isDragActive ? (
          <p>Drop the files here ...</p>
        ) : (
          <div className={styles.upload_container}>
            <p>Drag 'n' drop the dataset here, or click to select dataset</p>
            <MdCloudUpload className={styles.upload_icon} />
          </div>
        )}
        <ul>
          {files.map((file, i) => (
            <li key={i} className={styles.file_item}>
              <div className={styles.file_info}>
                <div className={styles.file_name}>{file.name}</div>
              </div>
              <div className={styles.file_size}>
                {(file.size / (1024 * 1024)).toFixed(2)} MB
              </div>
            </li>
          ))}
        </ul>
      </div>
      {files.length > 0 && (
        <button className={styles.upload_button} onClick={fileSubmitHandler}>
          Upload
        </button>
      )}
    </div>
  );
}

export default TestModel;
