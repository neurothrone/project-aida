import {drawGraph} from "./charts/draw.mjs";
import {getBarGraphOptions, getLineGraphOptions} from "./charts/options.mjs";

const baseUrl = "http://127.0.0.1:8000";
const heartEndPoint = `${baseUrl}/api/health/heart/chart/`;
const id = "heartGraph";
const options = getBarGraphOptions("Heart rate Graph", "Dates", "Pulse");

// const options = {
//     plugins: {
//         legend: {
//             display: true,
//             position: "top",
//             title: {
//                 display: true,
//                 text: "Heart rate Graph",
//                 padding: "10",
//                 color: 'rgba(150, 0, 255, 1)',
//                 font: {
//                     family: "sans-serif",
//                     style: "normal",
//                     weight: "900",
//                     lineHeight: 1.5,
//                     size: 20
//                 }
//             }
//         }
//     },
//     responsive: true,
//     scales: {
//         xAxes: {
//             title: {
//                 display: true,
//                 text: "Dates",
//                 align: "center",
//                 color: 'rgba(150, 0, 255, 1)',
//                 font: {
//                     family: "sans-serif",
//                     style: "normal",
//                     weight: "900",
//                     lineHeight: 1.5,
//                     size: 20
//                 },
//                 ticks: {
//                     beginAtZero: true,
//                 }
//             }
//         },
//         yAxes: {
//             title: {
//                 display: true,
//                 text: "Pulse",
//                 align: "center",  // start, center, end
//                 color: 'rgba(150, 0, 255, 1)',
//                 font: {
//                     family: "sans-serif",
//                     style: "normal",
//                     weight: "900",
//                     lineHeight: 1.5,
//                     size: 20
//                 }
//             },
//             beginAtZero: true
//         }
//     }
// }

drawGraph(heartEndPoint, id, options, "bar");
