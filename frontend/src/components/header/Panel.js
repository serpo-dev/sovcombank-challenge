import React, { useState } from "react";
import Authorized from "./Authorized";
import Anonym from "./Anonym";

const Panel = () => {
    const [isAuth, setIsAuth] = useState(true);

    if (isAuth) {
        return <Authorized />;
    }

    if (!isAuth) {
        return <Anonym />;
    }
};

export default Panel;
