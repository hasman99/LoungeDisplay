"""Python type stubs for the simple RGB matrix graphics helpers."""

from .core import Canvas


class Color:
    """RGB color value with 8-bit red, green, and blue channels."""

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        """Create a color from red, green, and blue channel values."""
        ...

    @property
    def red(self) -> int:
        """Red channel value."""
        ...

    @red.setter
    def red(self, value: int) -> None:
        """Set the red channel value."""
        ...

    @property
    def green(self) -> int:
        """Green channel value."""
        ...

    @green.setter
    def green(self, value: int) -> None:
        """Set the green channel value."""
        ...

    @property
    def blue(self) -> int:
        """Blue channel value."""
        ...

    @blue.setter
    def blue(self, value: int) -> None:
        """Set the blue channel value."""
        ...


class Font:
    """BDF font that can measure and draw Unicode glyphs."""

    def CharacterWidth(self, char: int) -> int:
        """Return the width of a Unicode codepoint in pixels.

        Returns -1 if the font is not loaded or the character does not exist.
        """
        ...

    def LoadFont(self, file: str) -> None:
        """Load a BDF font from ``file``.

        The font is only usable after this method succeeds.
        """
        ...

    def DrawGlyph(self, c: Canvas, x: int, y: int, color: Color, char: int) -> int:
        """Draw one Unicode codepoint onto a canvas.

        ``y`` is the font baseline. Returns the pixel advance, or 0 if no
        character was drawn.
        """
        ...

    @property
    def height(self) -> int:
        """Font height in pixels, or -1 if no font has been loaded."""
        ...

    @property
    def baseline(self) -> int:
        """Pixels from the top line to the font baseline."""
        ...


def DrawText(c: Canvas, f: Font, x: int, y: int, color: Color, text: str) -> int:
    """Draw UTF-8 text with a font and color.

    ``y`` is the font baseline. Returns the number of pixels advanced.
    """
    ...


def DrawCircle(c: Canvas, x: int, y: int, r: int, color: Color) -> None:
    """Draw a circle centered at ``(x, y)`` with radius ``r``."""
    ...


def DrawLine(
    c: Canvas,
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    color: Color,
) -> None:
    """Draw a line from ``(x1, y1)`` to ``(x2, y2)``."""
    ...
