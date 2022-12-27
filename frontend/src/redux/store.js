import { configureStore } from "@reduxjs/toolkit";
import accountReducer from "./accountReducer";
import catalogReducer from "./catalogReducer";

export default configureStore({
    reducer: {
        account: accountReducer,
        catalog: catalogReducer,
    },
});
