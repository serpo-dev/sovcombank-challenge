import React from "react";
import { block_dsbrd } from "../../../styles/main";
import Gradient from "./charts/Gradient";
import { h1 } from "../../../styles/main";

const Charts = () => {
    return (
        <div className={block_dsbrd}>
            <div className={h1}>Обзор</div>
            <Gradient />
        </div>
    );
};

export default Charts;
