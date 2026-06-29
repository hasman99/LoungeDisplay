import os
import sys
import time

from rgbmatrix import FrameCanvas, RGBMatrix, RGBMatrixOptions, graphics

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
FONT_PATH = os.path.join(PROJECT_ROOT, "rgbmatrix", "fonts", "5x7.bdf")


LINES = [
    "Line 1",
    "Line 2",
    "Line 3",
    "Line 4",
    "Line 5",
    "Line 6",
]


def create_matrix():
    options = RGBMatrixOptions()
    options.hardware_mapping = "regular"
    options.rows = 48
    options.cols = 96
    options.chain_length = 1
    options.parallel = 1
    options.pwm_bits = 11
    options.brightness = 60
    options.scan_mode = 1
    options.row_address_type = 0
    options.multiplexing = 0
    options.pwm_lsb_nanoseconds = 130
    options.led_rgb_sequence = "RGB"
    options.pixel_mapper_config = ""
    options.panel_type = ""
    options.pwm_dither_bits = 0
    options.limit_refresh_rate_hz = 0
    options.gpio_slowdown = 2
    options.rp1_rio = 0
    options.disable_hardware_pulsing = False
    options.show_refresh_rate = True
    options.inverse_colors = False
    options.drop_privileges = True
    options.drop_priv_user = "sam"
    options.drop_priv_group = "sam"

    return RGBMatrix(options=options)


def draw_lines(canvas: FrameCanvas, font, lines):
    canvas.Clear()

    text_color = graphics.Color(255, 255, 255)
    baseline_y = font.baseline
    line_spacing = 8

    for line in lines:
        graphics.DrawText(canvas, font, 0, baseline_y, text_color, line)
        baseline_y += line_spacing


def main():
    matrix = create_matrix()

    font = graphics.Font()
    font.LoadFont(FONT_PATH)

    canvas = matrix.CreateFrameCanvas()

    try:
        print("Press CTRL-C to stop.")
        while True:
            draw_lines(canvas, font, LINES)
            canvas = matrix.SwapOnVSync(canvas)
            time.sleep(0.1)
    except KeyboardInterrupt:
        matrix.Clear()
        sys.exit(0)


if __name__ == "__main__":
    main()
