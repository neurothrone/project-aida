import {drawGraph} from "./charts/draw.mjs";
import {getLineGraphOptions} from "./charts/options.mjs";

const baseUrl = "http://127.0.0.1:8000";
const sleepEndPoint = `${baseUrl}/api/health/sleep/chart/`;
const id = "sleepGraph";
const options = getLineGraphOptions("Hours slept per day Graph", "Dates", "Hours");

drawGraph(sleepEndPoint, id, options, "line");
