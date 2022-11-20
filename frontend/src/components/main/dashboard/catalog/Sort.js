import React, { useState } from "react";
import sort_arrows from "../../../../assets/sort_arrows.svg";
import { p_tbl, sort_tbl } from "../../../../styles/main";

const Sort = (props) => {
    let title;

    switch (props.name) {
        case "name":
            title = "Название";
            break;
        case "price":
            title = "Цена";
            break;
        case "today":
            title = "За день";
            break;
        case "year":
            title = "За год";
            break;
    }

    const showArrows = () => {
        if (props.name !== "name")
            return <img src={sort_arrows} className="h-4" />;
        else return null;
    };
    const arrows = showArrows();

    return (
        <div className={sort_tbl}>
            <p className={p_tbl}>{title}</p>
            {arrows}
        </div>
    );
};

export default Sort;
