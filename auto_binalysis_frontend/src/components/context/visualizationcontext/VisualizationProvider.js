import { createContext, useReducer, useState } from "react";
import reducer from "./Reducer";

export const visualizationContext = createContext();

const VisualizationProvider = ({ children }) => {
  const [initialState] = useState({ data: {}, model_name: "" });

  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <visualizationContext.Provider value={[state, dispatch]}>
      {children}
    </visualizationContext.Provider>
  );
};

export default VisualizationProvider;
