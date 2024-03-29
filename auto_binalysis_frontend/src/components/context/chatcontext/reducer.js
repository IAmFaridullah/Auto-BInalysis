const reducer = (state, action) => {
  switch (action.type) {
    case "ADD_CHAT_USERS":
      return { ...state, chatUsers: action.payload };
    case "SELECT_USER":
      return { ...state, selectedUser: action.payload };
    default:
      return;
  }
};

export default reducer;
