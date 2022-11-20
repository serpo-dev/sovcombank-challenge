import React from "react";
import { NavLink } from "react-router-dom";
import Logo from "./Logo";
import Name from "./Name";

import { label } from "../../styles/header";

const Label = () => {
    return (
        <NavLink to="/" className={label}>
            <Logo />
            <Name />
        </NavLink>
    );
};

export default Label;
