import axios from "axios";
import React, { useEffect, useState } from "react";

function Home() {
  const [user, setUser] = useState({});
  const accessToken = window.localStorage.getItem("accessToken");
  const getUserData = async () => {
    const response = await axios.get("http://localhost:8000/auth/users/me/", {
      headers: {
        Authorization: `JWT ${accessToken}`,
      },
    });
    console.log(response);
    setUser(response.data);
  };

  useEffect(() => {
    getUserData();
  }, []);

  return (
    <>
      <h1>{user?.name}</h1>
    </>
  );
}

export default Home;
