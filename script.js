const DISPLAY_WIDTH = 64;
const DISPLAY_HEIGHT = 32;
const ROW_HEIGHT = 8;
const TEXT_HEIGHT = 7;

const rows = [
  "Hello World",
  "Hello World",
  "Hello World",
  "Hello World",
];

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

  rows.slice(0, 4).forEach((text, rowIndex) => drawText(buffer, text, rowIndex));

  matrix.innerHTML = "";

  for (let y = 0; y < DISPLAY_HEIGHT; y += 1) {
    for (let x = 0; x < DISPLAY_WIDTH; x += 1) {
      const dot = document.createElement("span");
      dot.className = buffer[y][x] ? "dot is-on" : "dot";
      matrix.appendChild(dot);
    }
  }
}

renderDisplay();
