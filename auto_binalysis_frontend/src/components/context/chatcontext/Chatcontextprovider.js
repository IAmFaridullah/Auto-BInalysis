import { createContext, useReducer, useState } from "react";
import reducer from "./reducer";

export const chatContext = createContext();

const ChatContextProvider = ({ children }) => {
  const [initialState] = useState({ users: [], selectedUser: {} });

  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <chatContext.Provider value={[state, dispatch]}>
      {children}
    </chatContext.Provider>
  );
};

export default ChatContextProvider;
