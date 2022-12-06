import React from "react";
import Catalog from "./Catalog";
import History from "./History";
import Accounts from "./Accounts";
import Charts from "./Charts";
import Diagram from "./Diagram";

const Dashboard = () => {
    return (
        <div className="grid grid-cols-6 pt-16 w-[1200px] space-x-2">
            <div className="col-span-4">
                <Catalog />
            </div>
            <div className="col-span-2">
                <Charts />
            </div>
            <div className="col-span-2">
                <History />
            </div>
            <div className="col-span-2">
                <Accounts />
            </div>
            <div className="col-span-2">
                <Diagram />
            </div>
        </div>
    );
};

export default Dashboard;
