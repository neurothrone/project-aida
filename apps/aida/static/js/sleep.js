import {drawLineGraph} from "./charts/line.mjs";
import {drawBarGraph} from "./charts/bar.mjs";

const baseUrl = "http://127.0.0.1:8000";
const sleepEndPoint = `${baseUrl}/api/health/sleep/chart/`;

const id = "sleepGraph";
const options = {
    plugins: {
        legend: {
            display: true,
            position: "top",
            title: {
                display: true,
                text: "Hours slept per day Graph",
                padding: "10",
                color: 'rgba(150, 0, 255, 1)',
                font: {
                    family: "sans-serif",
                    style: "normal",
                    weight: "900",
                    lineHeight: 1.5,
                    size: 20
                }
            }
        }
    },
    responsive: true,
    scales: {
        xAxes: {
            title: {
                display: true,
                text: "Dates",
                align: "center",
                color: 'rgba(150, 0, 255, 1)',
                font: {
                    family: "sans-serif",
                    style: "normal",
                    weight: "900",
                    lineHeight: 1.5,
                    size: 20
                },
                ticks: {
                    beginAtZero: true,
                }
            }
        },
        yAxes: {
            title: {
                display: true,
                text: "Hours",
                align: "center",  // start, center, end
                color: 'rgba(150, 0, 255, 1)',
                font: {
                    family: "sans-serif",
                    style: "normal",
                    weight: "900",
                    lineHeight: 1.5,
                    size: 20
                }
            },
            beginAtZero: true
        }
    }
}

function drawSleepGraph(endpoint, id, options, type = "line") {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            switch (type) {
                case "line":
                    drawLineGraph(data, id, options);
                    break;
                case "bar":
                    drawBarGraph(data, id);
                    break;
            }
        })
        .catch((error) => {
            console.error(`Something went wrong with drawSleepGraph(). Error: ${error}`);
        });
}

drawSleepGraph(sleepEndPoint, id, options);
