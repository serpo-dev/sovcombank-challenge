import React, { useState } from "react";

import ReactApexChart from "react-apexcharts";

const Gradient = (props) => {
    const [state, setState] = useState({
        series: [
            {
                name: "Sales",
                data: [
                    4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7,
                    5,
                ],
            },
        ],
        xaxis: {},
        dataLables: {
            style: {
                fontSize: '14px',
                fontFamily: 'Helvetica, Arial, sans-serif',
                fontWeight: 'bold',
                colors: ['#fff']
            },
        },
        options: {
            chart: {
                toolbar: { show: false },
                height: 350,
                type: "line",
            },

            stroke: {
                width: 5,
                curve: "smooth",
            },
            fill: {
                type: "gradient",
                gradient: {
                    shade: "dark",
                    gradientToColors: ["#FDD835"],
                    shadeIntensity: 1,
                    type: "horizontal",
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0, 100, 100, 100],
                },
            },
        },
    });

    return (
        <div id="chart">
            <ReactApexChart
                options={state.options}
                series={state.series}
                type="line"
                height={350}
            />
        </div>
    );
};

export default Gradient;
