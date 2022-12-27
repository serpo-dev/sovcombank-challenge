import React from "react";
import { bg_gradient_wndw, border_wndw } from "../../../styles/main";
import WindowBody from "./WindowBody";
import WindowLine from "./WindowLine";
import WindowTitle from "./WindowTitle";

const Window = (props) => {
    const type = props.type;

    return (
        <div className={border_wndw}>
            <div className={bg_gradient_wndw}>
                <div className="flex flex-col">
                    <WindowTitle type={type} />
                    <WindowLine />
                    <WindowBody type={type} />
                </div>
            </div>
        </div>
    );
};

export default Window;
