import React from "react";
import HistoryBody from "./window/HistoryBody";
import HistoryTitle from "./window/HistoryTitle";
import AccountsTitle from "./window/AccountsTitle";
import AccountsBody from "./window/AccountsBody";

const Window = (props) => {
    const type = props.type;

    return (
        <div className="border-[1px] border-[#A5A5A5] h-full w-full rounded-lg">
            <div className="bg-gradient-to-t from-[rgba(165,165,165,0.5)] to-transparent">
                <div className="flex flex-col">
                    <div className="p-2 flex justify-center">
                        {type === "accounts" ? (
                            <AccountsTitle />
                        ) : (
                            <HistoryTitle />
                        )}
                    </div>
                    <div className="h-[1px] bg-[#a5a5a5] w-full mt-2 mb-2" />
                    <div className="p-2 flex justify-center">
                        {type === "accounts" ? (
                            <AccountsBody />
                        ) : (
                            <HistoryBody />
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Window;
