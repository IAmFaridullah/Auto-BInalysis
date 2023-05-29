const Reducer = (state, action) => {
  switch (action.type) {
    case "SET_DATA":
      return { ...state, data: action.payload };
    case "SET_MODEL_NAME":
      return { ...state, model_name: action.payload };
    default:
      return;
  }
};

export default Reducer;
