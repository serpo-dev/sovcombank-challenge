import React from "react";
import { NavLink } from "react-router-dom";

import { h1_hdr } from "../../styles/header";
import { panel } from "../../styles/header";

const Authorized = () => {
    return (
        <div className={panel}>
            <div className={h1_hdr}>
                <NavLink to="/account">Личный кабинет</NavLink>
            </div>
            <div className={h1_hdr}>
                <button>Выйти</button>
            </div>
        </div>
    );
};

export default Authorized;
