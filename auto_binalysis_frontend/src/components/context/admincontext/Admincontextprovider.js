import { createContext, useReducer, useState } from "react";
import reducer from "./reducer";

export const AdminContext = createContext();

const AdminContextProvider = ({ children }) => {
  const [initialState] = useState({ users: [], selectedUser: {} });

  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <AdminContext.Provider value={[state, dispatch]}>
      {children}
    </AdminContext.Provider>
  );
};

export default AdminContextProvider;
