import React from "react";
import Line from "./Line";
import Sort from "./Sort";
import { title_tbl } from "../../../../styles/main";

const Title = () => {
    return (
        <div>
            <div className={title_tbl}>
                <div className="grow">
                    <Sort name="name" />
                </div>
                <div>
                    <Sort name="price" />
                </div>
                <div>
                    <Sort name="today" />
                </div>
                <div>
                    <Sort name="year" />
                </div>
            </div>
            <Line />
        </div>
    );
};

export default Title;
