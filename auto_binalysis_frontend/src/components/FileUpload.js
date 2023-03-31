import axios from "axios";
import styles from "./css/FileUpload.module.css";
import React, { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { MdCloudUpload } from "react-icons/md";

function FileUpload({ url }) {
  const [files, setFiles] = useState([]);
  const user = JSON.parse(localStorage.getItem("user"));

  const onDrop = useCallback((acceptedFiles) => {
    setFiles(files.concat(acceptedFiles));
    // Do something with the files
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  const fileSubmitHandler = async () => {
    const formData = new FormData();
    formData.append("file", files[0]);
    formData.append("username", user.username);
    const response = await axios.post(
      url,
      formData
    );
    if (response.status === 200) {
      console.log(response);
    }
  };

  return (
    <div className={styles.dropzone_container}>
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

export default FileUpload;
