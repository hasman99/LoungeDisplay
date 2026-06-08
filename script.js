const DISPLAY_WIDTH = 128;
const DISPLAY_HEIGHT = 64;
const ROW_HEIGHT = 8;
const TEXT_HEIGHT = 7;
const VISIBLE_ROW_COUNT = DISPLAY_HEIGHT / ROW_HEIGHT;
const SECTION_ROW_COUNT = VISIBLE_ROW_COUNT / 2;
const TFL_STOP_POINT_ID = "490012394W";
const TFL_APP_KEY = "ad941341170745109559d8d9f62a5aa5";
const TFL_POLL_INTERVAL_MS = 60 * 1000;
const HUXLEY_DEPARTURES_URL = "http://localhost:8081/departures/NEM/to/WAT/10";
const HUXLEY_DESTINATION_CRS = "WAT";
const HUXLEY_POLL_INTERVAL_MS = 60 * 1000;

let busRows = ["Loading", "buses"];
let trainRows = ["Loading", "trains"];
const rows = [...busRows, ...trainRows];

const FONT_5X7 = {
  " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
  A: ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
  B: ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
  C: ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
  D: ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
  E: ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
  F: ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
  G: ["01110", "10001", "10000", "10111", "10001", "10001", "01110"],
  H: ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
  I: ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
  J: ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
  K: ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
  L: ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
  M: ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
  N: ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
  O: ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
  P: ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
  Q: ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
  R: ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
  S: ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
  T: ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
  U: ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
  V: ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
  W: ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
  X: ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
  Y: ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
  Z: ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
  "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
  "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
  "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
  "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
  "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
  "5": ["11111", "10000", "10000", "11110", "00001", "00001", "11110"],
  "6": ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
  "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
  "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
  "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
  ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
  ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
  "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
};

function createDisplayBuffer() {
  return Array.from({ length: DISPLAY_HEIGHT }, () => Array(DISPLAY_WIDTH).fill(false));
}

function drawText(buffer, text, rowIndex) {
  const yOffset = rowIndex * ROW_HEIGHT;
  let xOffset = 0;

  for (const character of text.toUpperCase()) {
    const glyph = FONT_5X7[character] || FONT_5X7[" "];
    const glyphWidth = glyph[0].length;

    if (xOffset >= DISPLAY_WIDTH) {
      break;
    }

    for (let y = 0; y < TEXT_HEIGHT; y += 1) {
      for (let x = 0; x < glyphWidth; x += 1) {
        const displayX = xOffset + x;
        const displayY = yOffset + y;

        if (displayX < DISPLAY_WIDTH && glyph[y][x] === "1") {
          buffer[displayY][displayX] = true;
        }
      }
    }

    xOffset += character === " " ? 4 : glyphWidth + 1;
  }
}

function renderDisplay() {
  const matrix = document.getElementById("dot-matrix");
  const buffer = createDisplayBuffer();

  rows.slice(0, VISIBLE_ROW_COUNT).forEach((text, rowIndex) => drawText(buffer, text, rowIndex));

  matrix.innerHTML = "";

  for (let y = 0; y < DISPLAY_HEIGHT; y += 1) {
    for (let x = 0; x < DISPLAY_WIDTH; x += 1) {
      const dot = document.createElement("span");
      dot.className = buffer[y][x] ? "dot is-on" : "dot";
      matrix.appendChild(dot);
    }
  }
}

function setRows(nextRows) {
  rows.splice(0, rows.length, ...nextRows.slice(0, VISIBLE_ROW_COUNT));

  while (rows.length < VISIBLE_ROW_COUNT) {
    rows.push("");
  }

  renderDisplay();
}

function getSectionRows(nextRows) {
  const sectionRows = nextRows.slice(0, SECTION_ROW_COUNT);

  while (sectionRows.length < SECTION_ROW_COUNT) {
    sectionRows.push("");
  }

  return sectionRows;
}

function setBusRows(nextRows) {
  busRows = getSectionRows(nextRows);
  setRows([...busRows, ...trainRows]);
}

function setTrainRows(nextRows) {
  trainRows = getSectionRows(nextRows);
  setRows([...busRows, ...trainRows]);
}

function formatArrivalTime(secondsToArrival) {
  const minutesToArrival = Math.max(0, Math.round(secondsToArrival / 60));

  return minutesToArrival <= 1 ? "DUE" : `${minutesToArrival} MIN`;
}

function formatArrival(arrival) {
  return `${arrival.lineName} ${formatArrivalTime(arrival.timeToStation)}`;
}

function compactTrainTime(time) {
  return String(time ?? "")
    .replace("*", "")
    .trim()
    .toUpperCase();
}

function formatDepartureEstimate(departure) {
  const estimatedDeparture = String(departure.etd ?? "").trim();
  const normalizedEstimate = estimatedDeparture.toUpperCase();

  if (
    departure.isCancelled ||
    departure.filterLocationCancelled ||
    normalizedEstimate.includes("CANCEL")
  ) {
    return "CANCELLED";
  }

  if (normalizedEstimate === "ON TIME") {
    return "ON TIME";
  }

  if (normalizedEstimate === "DELAYED") {
    return "DELAYED";
  }

  if (normalizedEstimate === "NO REPORT") {
    return "NO REPORT";
  }

  return compactTrainTime(estimatedDeparture) || "---";
}

function formatDeparture(departure) {
  const scheduledDeparture = compactTrainTime(departure.std) || "--:--";

  return `${scheduledDeparture} ${formatDepartureEstimate(departure)}`;
}

function isDepartureToDestination(departure) {
  return (departure.destination || []).some(
    (destination) => destination.crs === HUXLEY_DESTINATION_CRS,
  );
}

function getArrivalsUrl() {
  const url = new URL(`https://api.tfl.gov.uk/StopPoint/${TFL_STOP_POINT_ID}/Arrivals`);
  url.searchParams.set("app_key", TFL_APP_KEY);

  return url;
}

async function updateArrivals() {
  try {
    const response = await fetch(getArrivalsUrl());

    if (!response.ok) {
      throw new Error(`TfL returned ${response.status}`);
    }

    const arrivals = await response.json();
    const upcomingArrivals = arrivals
      .filter((arrival) => Number.isFinite(arrival.timeToStation))
      .sort((a, b) => a.timeToStation - b.timeToStation)
      .slice(0, SECTION_ROW_COUNT)
      .map(formatArrival);

    setBusRows(upcomingArrivals.length > 0 ? upcomingArrivals : ["No buses", "listed"]);
  } catch (error) {
    setBusRows(["TfL error", "Retry 1m"]);
    console.error(error);
  }
}

async function updateDepartures() {
  try {
    const response = await fetch(HUXLEY_DEPARTURES_URL);

    if (!response.ok) {
      throw new Error(`Huxley returned ${response.status}`);
    }

    const departureBoard = await response.json();
    const upcomingDepartures = (departureBoard.trainServices || [])
      .filter((departure) => departure && departure.std)
      .filter(isDepartureToDestination)
      .slice(0, SECTION_ROW_COUNT)
      .map(formatDeparture);

    setTrainRows(upcomingDepartures.length > 0 ? upcomingDepartures : ["No trains", "listed"]);
  } catch (error) {
    setTrainRows(["Rail error", "Retry 1m"]);
    console.error(error);
  }
}

renderDisplay();
updateArrivals();
updateDepartures();
setInterval(updateArrivals, TFL_POLL_INTERVAL_MS);
setInterval(updateDepartures, HUXLEY_POLL_INTERVAL_MS);
