import USD from "../assets/countries/USD.svg";
import EUR from "../assets/countries/EUR.svg";
import GBP from "../assets/countries/GBP.svg";
import CHF from "../assets/countries/CHF.svg";
import CNY from "../assets/countries/CNY.svg";
import JPY from "../assets/countries/JPY.svg";

const initialState = {
    data: [
        {
            name: "USD",
            image: USD,
            price: "60.59 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-13,0425 P",
            year_pc: "17,16%",
        },
        {
            name: "EUR",
            image: EUR,
            price: "62.6 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-20,575 P",
            year_pc: "24.78%",
        },
        {
            name: "GBP",
            image: GBP,
            price: "62.6 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-20,575 P",
            year_pc: "24.78%",
        },
        {
            name: "CHF",
            image: CHF,
            price: "62.6 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-20,575 P",
            year_pc: "24.78%",
        },
        {
            name: "CNY",
            image: CNY,
            price: "62.6 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-20,575 P",
            year_pc: "24.78%",
        },
        {
            name: "JPY",
            image: JPY,
            price: "62.6 P",
            today_rub: "0 P",
            today_pc: "0%",
            year_rub: "-20,575 P",
            year_pc: "24.78%",
        },
    ],
};

const actionTypes = {};

const catalogReducer = (state = initialState, action) => {
    switch (action.type) {
        default:
            return state;
    }
};

export default catalogReducer;
