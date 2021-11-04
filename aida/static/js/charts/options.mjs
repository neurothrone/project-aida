function getBarGraphOptions(title, xLabel, yLabel) {
    return {
        plugins: {
            legend: {
                display: true,
                position: "top",
                labels: {
                    color: 'rgba(150, 0, 255, 1)',
                    font: {
                        size: 14,
                        weight: 800
                    }
                },
                title: {
                    display: true,
                    text: title,
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
                    text: xLabel,
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
                },
                ticks: {
                    color: "black",
                    font: {
                        size: 14,
                        weight: 800
                    }
                }
            },
            yAxes: {
                title: {
                    display: true,
                    text: yLabel,
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
}

function getLineGraphOptions(title, xLabel, yLabel) {
    return {
        plugins: {
            legend: {
                display: true,
                position: "top",
                title: {
                    display: true,
                    text: title,
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
                    text: xLabel,
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
                    text: yLabel,
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
}

export {getBarGraphOptions};
export {getLineGraphOptions};