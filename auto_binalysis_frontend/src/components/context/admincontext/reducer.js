const reducer = (state, action) => {
  switch (action.type) {
    case "ADD_ADMIN_USERS":
      return { ...state, users: action.payload };
    case "SELECT_USER":
      return { ...state, selectedUser: action.payload };
    default:
      return;
  }
};

export default reducer;
