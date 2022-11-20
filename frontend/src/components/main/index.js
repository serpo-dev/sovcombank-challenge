import React from "react";
import { Route, Routes } from "react-router-dom";
import Account from "./account";
import Invoice from "./invoice";
import Dashboard from "./dashboard";

const Main = () => {
    return (
        <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/account" element={<Account />} />
            <Route path="/invoice/*" element={<Invoice />} />
        </Routes>
    );
};

export default Main;
