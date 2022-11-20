import React, { useState } from "react";
import Row from "./Row";
import Title from "./Title";

const Table = () => {
    const data = [
        {
            name: "USD",
            price: "60.59 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-13,0425 P",
            year_pc: "17,16%",
        },
        {
            name: "EUR",
            price: "62.6 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-20,575 P",
            year_pc: "24.78%",
        },
    ];

    const rows = data.map((elem) => <Row data={elem} />);
    console.log(rows);

    return (
        <div>
            <Title />
            {rows}
        </div>
    );
};

export default Table;
