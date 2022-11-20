import React from "react";
import { NavLink } from "react-router-dom";

import { h1_hdr } from "../../styles/header";
import { panel } from "../../styles/header";

const Anonym = () => {
    return (
        <div className={h1_hdr}>
            <div className={panel}>
                <NavLink to="login">Войти</NavLink>
                <NavLink to="registration">Зарегистрироваться</NavLink>
            </div>
        </div>
    );
};

export default Anonym;
