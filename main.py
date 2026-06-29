import sys
import time

from PIL import Image

from rgbmatrix import RGBMatrix, RGBMatrixOptions


def main():

    image = Image.open(
        "/home/sam/Documents/LoungeDisplay/628dacc0-79dd-11ef-aa47-5d501e31b93c.jpg"
    )

    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 48
    options.cols = 96
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = "regular"  # If you have an Adafruit HAT: 'adafruit-hat'

    matrix = RGBMatrix(options=options)

    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.Resampling.LANCZOS)

    matrix.SetImage(image.convert("RGB"))

    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
