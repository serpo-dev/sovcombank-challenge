import React from "react";
import HistoryTitle from "./window/HistoryTitle";
import AccountsTitle from "./window/AccountsTitle";

const WindowTitle = (props) => {
    const type = props.type;

    return (
        <div className="p-2 flex justify-center">
            {type === "accounts" ? <AccountsTitle /> : <HistoryTitle />}
        </div>
    );
};

export default WindowTitle;
