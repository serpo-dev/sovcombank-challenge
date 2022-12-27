import React from "react";
import AccountsBody from "./window/AccountsBody";
import HistoryBody from "./window/HistoryBody";

const WindowBody = (props) => {
    const type = props.type;

    return (
        <div className="p-2 flex justify-center">
            {type === "accounts" ? <AccountsBody /> : <HistoryBody />}
        </div>
    );
};

export default WindowBody;
