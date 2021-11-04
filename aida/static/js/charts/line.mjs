import {defaultOptions} from "./shared.mjs";

function drawLineGraph(data, id, options = defaultOptions) {
    let ctx = document.getElementById(id).getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: data.chart_label,
                data: data.chart_data,
                backgroundColor: 'rgba(150, 0, 255, 0.5)',
                pointBackgroundColor: "rgba(50, 0, 255, 0.6)",
                borderColor: 'rgba(100, 0, 255, 0.2)',
                fill: true,
            }],
        },
        options: options
    });
}

export {drawLineGraph};