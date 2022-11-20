import React from "react";
import { row_tbl } from "../../../../styles/main";
import Line from "./Line";
import { p, grid_tbl } from "../../../../styles/main";

const Row = (props) => {
    const data = props.data;

    const grown_grid = `grow ${grid_tbl}`;

    return (
        <div>
            <div className={row_tbl}>
                <div className={grown_grid}>
                    <div className={p}>{data.name}</div>
                </div>
                <div className={grid_tbl}>
                    <div className={p}>{data.price}</div>
                </div>
                <div className={grid_tbl}>
                    <div className={p}>{data.today_rub}</div>
                </div>
                <div className={grid_tbl}>
                    <div className={p}>{data.year_rub}</div>
                </div>
            </div>
            <Line />
        </div>
    );
};

export default Row;
