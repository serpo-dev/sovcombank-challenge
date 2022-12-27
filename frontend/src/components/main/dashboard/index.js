import React from "react";
import Catalog from "./Catalog";
import History from "./History";
import Accounts from "./Accounts";
import Charts from "./Charts";
import Diagram from "./Diagram";

const Dashboard = () => {
    return (
        <div className="grid grid-cols-6 pt-16 w-[1200px]">
            <div className="col-span-3">
                <Catalog />
            </div>
            <div className="col-span-3">
                <Charts />
            </div>
            <div className="col-span-2 mr-8">
                <Accounts />
            </div>
            <div className="col-span-2 ml-4 mr-4">
                <History />
            </div>
            <div className="col-span-2 ml-8">
                <Diagram />
            </div>
        </div>
    );
};

export default Dashboard;
