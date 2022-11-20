import React from "react";
import Label from "./Label";
import Panel from "./Panel";

const Header = () => {
    return (
        <div className="h-20 p-6">
            <span className="flex flex-row items-center w-[1200px]">
                <Label className="w-40" />
                <span className="grow" />
                <Panel className="w-40" />
            </span>
        </div>
    );
};

export default Header;
