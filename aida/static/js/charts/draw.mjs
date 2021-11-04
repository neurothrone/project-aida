import {drawLineGraph} from "./line.mjs";
import {drawBarGraph} from "./bar.mjs";

function drawGraph(endpoint, id, options, type = "line") {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            switch (type) {
                case "line":
                    drawLineGraph(data, id, options);
                    break;
                case "bar":
                    drawBarGraph(data, id, options);
                    break;
            }
        })
        .catch((error) => {
            console.error(`Something went wrong with drawGraph(). Error: ${error}`);
        });
}

export {drawGraph};