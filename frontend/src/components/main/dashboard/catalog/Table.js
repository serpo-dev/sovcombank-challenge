import React from "react";
import { useSelector } from "react-redux";
import Row from "./Row";
import Title from "./Title";

const Table = () => {
    const data = useSelector((state) => state.catalog.data);

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
