import React from "react";
import { block_dsbrd, h1 } from "../../../styles/main";
import Table from "./catalog/Table";
import { catalog_dsbrd } from "../../../styles/main";

const Catalog = () => {
    return (
        <div className={block_dsbrd}>
            <div className={catalog_dsbrd}>
                <p className={h1}>Каталог валюты</p>
                <Table />
            </div>
        </div>
    );
};

export default Catalog;
