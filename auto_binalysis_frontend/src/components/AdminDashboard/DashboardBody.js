import React, { useContext, useEffect, useState } from "react";

import styles from "./DashboardBody.module.css";
import { Table, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { AdminContext } from "../context/admincontext/Admincontextprovider";

function DashboardBody() {
  const navigate = useNavigate();
  const [state, dispatch] = useContext(AdminContext);

  const getUsers = async () => {
    const response = await axios.get("http://localhost:8000/adminpanel/users/");
    if (response.status === 200) {
      dispatch({
        type: "ADD_ADMIN_USERS",
        payload: response.data.users,
      });
    }
  };
  useEffect(() => {
    getUsers();
  }, []);

  const deleteUserHandler = async (username) => {
    const response = await axios.post(
      "http://localhost:8000/adminpanel/delete-user/",
      {
        username: `${username}`,
      }
    );
    if (response.status === 200) {
      const updatedUsers = state?.users.filter(
        (user) => user.username !== username
      );
      dispatch({
        type: "ADD_ADMIN_USERS",
        payload: updatedUsers,
      });
    }
  };

  const EditUserHandler = (user) => {
    dispatch({
      type: "SELECT_USER",
      payload: user,
    });
    navigate(`/admin/update-user/${user.username}`);
  };

  return (
    <div className={styles.container}>
      <Table striped bordered hover>
        <thead>
          <tr className={styles.table_row}>
            <th>#</th>
            <th>Name</th>
            <th>Email</th>
            <th>Country</th>
          </tr>
        </thead>
        <tbody className={styles.table_body}>
          {state?.users.map((user, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td>{user.country ? user.country : "NA"}</td>
              <td>
                <Button
                  variant="success"
                  style={{ marginRight: "5px" }}
                  onClick={() => EditUserHandler(user)}
                >
                  Edit
                </Button>
                <Button
                  variant="danger"
                  onClick={() => deleteUserHandler(user.username)}
                >
                  Remove
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default DashboardBody;
