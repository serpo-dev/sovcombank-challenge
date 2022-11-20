const initialState = {
    id: "0000 0000 0000 0000",
    number: "0",
    currency: "RUB",
};

const actionTypes = {
    CREATE: "CREATE",
};

const accountReducer = (state = initialState, action) => {
    switch (action.type) {
        case actionTypes.CREATE:
            const newState = {
                ...state,
            };
        default:
            return state;
    }
};

export default accountReducer;
