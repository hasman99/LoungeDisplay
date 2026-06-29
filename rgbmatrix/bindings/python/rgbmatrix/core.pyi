"""Python type stubs for the core RGB matrix canvas bindings."""

from typing import Any


class Canvas:
    """Interface for drawable RGB matrix canvases.

    A canvas represents a pixel surface that can be implemented by the live
    RGBMatrix or by an off-screen FrameCanvas.
    """

    def SetImage(
        self,
        image: Any,
        offset_x: int = 0,
        offset_y: int = 0,
        unsafe: bool = True,
    ) -> None:
        """Draw a Pillow RGB image onto the canvas at the given offset.

        The image is cropped at canvas edges. Offsets may be negative to shift
        the image partially outside the top or left edge.
        """
        ...

    def SetPixelsPillow(
        self,
        xstart: int,
        ystart: int,
        width: int,
        height: int,
        image_capsule: object,
    ) -> None:
        """Copy RGB pixels from a Pillow image capsule into the canvas.

        This is the fast path used by SetImage() when unsafe mode is enabled.
        """
        ...


class FrameCanvas(Canvas):
    """Off-screen canvas owned by an RGBMatrix for double or multi-buffering."""

    def Fill(self, red: int, green: int, blue: int) -> None:
        """Fill the entire frame with the given 24-bit RGB color."""
        ...

    def Clear(self) -> None:
        """Clear the frame to black."""
        ...

    def SetPixel(self, x: int, y: int, red: int, green: int, blue: int) -> None:
        """Set one pixel at ``(x, y)`` to the given 24-bit RGB color."""
        ...

    @property
    def width(self) -> int:
        """Canvas width in pixels."""
        ...

    @property
    def height(self) -> int:
        """Canvas height in pixels."""
        ...

    @property
    def pwmBits(self) -> int:
        """PWM bit depth used for this frame."""
        ...

    @pwmBits.setter
    def pwmBits(self, pwmBits: int) -> None:
        """Set this frame's PWM bit depth.

        Lower values use less CPU and may be sufficient for simple colors.
        """
        ...

    @property
    def brightness(self) -> int:
        """Frame brightness percentage."""
        ...

    @brightness.setter
    def brightness(self, val: int) -> None:
        """Set frame brightness as a percentage."""
        ...


class RGBMatrixOptions:
    """Matrix and runtime options used when constructing an RGBMatrix."""

    @property
    def hardware_mapping(self) -> str:
        """Hardware mapping name, such as ``regular`` or ``adafruit-hat``."""
        ...

    @hardware_mapping.setter
    def hardware_mapping(self, value: str) -> None:
        """Set the hardware mapping name."""
        ...

    @property
    def rows(self) -> int:
        """Number of rows supported by each display panel."""
        ...

    @rows.setter
    def rows(self, value: int) -> None:
        """Set the number of rows supported by each display panel."""
        ...

    @property
    def cols(self) -> int:
        """Number of columns per panel."""
        ...

    @cols.setter
    def cols(self, value: int) -> None:
        """Set the number of columns per panel."""
        ...

    @property
    def chain_length(self) -> int:
        """Number of displays daisy-chained together."""
        ...

    @chain_length.setter
    def chain_length(self, value: int) -> None:
        """Set the number of daisy-chained displays."""
        ...

    @property
    def parallel(self) -> int:
        """Number of parallel chains connected to the Raspberry Pi."""
        ...

    @parallel.setter
    def parallel(self, value: int) -> None:
        """Set the number of parallel chains."""
        ...

    @property
    def pwm_bits(self) -> int:
        """PWM bit depth used for output."""
        ...

    @pwm_bits.setter
    def pwm_bits(self, value: int) -> None:
        """Set the PWM bit depth used for output."""
        ...

    @property
    def pwm_lsb_nanoseconds(self) -> int:
        """Base on-time, in nanoseconds, for the lowest PWM bit."""
        ...

    @pwm_lsb_nanoseconds.setter
    def pwm_lsb_nanoseconds(self, value: int) -> None:
        """Set the base on-time, in nanoseconds, for the lowest PWM bit."""
        ...

    @property
    def brightness(self) -> int:
        """Initial panel brightness percentage."""
        ...

    @brightness.setter
    def brightness(self, value: int) -> None:
        """Set initial panel brightness as a percentage."""
        ...

    @property
    def scan_mode(self) -> int:
        """Scan mode: 0 for progressive, 1 for interlaced."""
        ...

    @scan_mode.setter
    def scan_mode(self, value: int) -> None:
        """Set the scan mode: 0 for progressive, 1 for interlaced."""
        ...

    @property
    def multiplexing(self) -> int:
        """Panel multiplexing type."""
        ...

    @multiplexing.setter
    def multiplexing(self, value: int) -> None:
        """Set the panel multiplexing type."""
        ...

    @property
    def row_address_type(self) -> int:
        """Row address type used by the panel."""
        ...

    @row_address_type.setter
    def row_address_type(self, value: int) -> None:
        """Set the panel row address type."""
        ...

    @property
    def disable_hardware_pulsing(self) -> bool:
        """Whether PWM hardware pulse generation is disabled."""
        ...

    @disable_hardware_pulsing.setter
    def disable_hardware_pulsing(self, value: bool) -> None:
        """Enable or disable PWM hardware pulse generation."""
        ...

    @property
    def show_refresh_rate(self) -> bool:
        """Whether to print the refresh rate for debugging and tuning."""
        ...

    @show_refresh_rate.setter
    def show_refresh_rate(self, value: bool) -> None:
        """Enable or disable refresh-rate output."""
        ...

    @property
    def inverse_colors(self) -> bool:
        """Whether panel colors are inverted."""
        ...

    @inverse_colors.setter
    def inverse_colors(self, value: bool) -> None:
        """Enable or disable inverted panel colors."""
        ...

    @property
    def led_rgb_sequence(self) -> str:
        """Physical LED color order as a three-character RGB permutation."""
        ...

    @led_rgb_sequence.setter
    def led_rgb_sequence(self, value: str) -> None:
        """Set the physical LED color order."""
        ...

    @property
    def pixel_mapper_config(self) -> str:
        """Semicolon-separated pixel mapper configuration."""
        ...

    @pixel_mapper_config.setter
    def pixel_mapper_config(self, value: str) -> None:
        """Set the pixel mapper configuration."""
        ...

    @property
    def panel_type(self) -> str:
        """Special panel type requiring custom initialization, if any."""
        ...

    @panel_type.setter
    def panel_type(self, value: str) -> None:
        """Set the special panel type, such as ``FM6126A``."""
        ...

    @property
    def pwm_dither_bits(self) -> int:
        """Number of lower PWM bits to time-dither for refresh rate."""
        ...

    @pwm_dither_bits.setter
    def pwm_dither_bits(self, value: int) -> None:
        """Set how many lower PWM bits are time-dithered."""
        ...

    @property
    def limit_refresh_rate_hz(self) -> int:
        """Refresh-rate limit in hertz; non-positive values mean no limit."""
        ...

    @limit_refresh_rate_hz.setter
    def limit_refresh_rate_hz(self, value: int) -> None:
        """Set the refresh-rate limit in hertz."""
        ...

    @property
    def gpio_slowdown(self) -> int:
        """GPIO slowdown setting; 0 means no slowdown."""
        ...

    @gpio_slowdown.setter
    def gpio_slowdown(self, value: int) -> None:
        """Set the GPIO slowdown value."""
        ...

    @property
    def rp1_rio(self) -> int:
        """RP1 backend selection: 0 for default PIO, 1 for RIO."""
        ...

    @rp1_rio.setter
    def rp1_rio(self, value: int) -> None:
        """Set the RP1 backend selection."""
        ...

    @property
    def daemon(self) -> int:
        """Daemon mode: -1 disabled, 0 foreground, 1 background."""
        ...

    @daemon.setter
    def daemon(self, value: int) -> None:
        """Set daemon mode."""
        ...

    @property
    def drop_privileges(self) -> int:
        """Privilege dropping mode: -1 disabled, 0 off, 1 on."""
        ...

    @drop_privileges.setter
    def drop_privileges(self, value: int) -> None:
        """Set privilege dropping mode."""
        ...

    @property
    def drop_priv_user(self) -> str:
        """User to switch to after initializing hardware."""
        ...

    @drop_priv_user.setter
    def drop_priv_user(self, value: str) -> None:
        """Set the user to switch to after initializing hardware."""
        ...

    @property
    def drop_priv_group(self) -> str:
        """Group to switch to after initializing hardware."""
        ...

    @drop_priv_group.setter
    def drop_priv_group(self, value: str) -> None:
        """Set the group to switch to after initializing hardware."""
        ...


class RGBMatrix(Canvas):
    """Live RGB matrix display and active framebuffer.

    The matrix implements Canvas directly, but drawing to the active display can
    tear. Prefer CreateFrameCanvas() and SwapOnVSync() for animations.
    """

    def __init__(
        self,
        rows: int = 0,
        chains: int = 0,
        parallel: int = 0,
        options: RGBMatrixOptions | None = None,
    ) -> None:
        """Create a matrix from options or from simple row/chain defaults."""
        ...

    def Fill(self, red: int, green: int, blue: int) -> None:
        """Fill the active framebuffer with the given 24-bit RGB color."""
        ...

    def SetPixel(self, x: int, y: int, red: int, green: int, blue: int) -> None:
        """Set one active-framebuffer pixel to the given 24-bit RGB color."""
        ...

    def Clear(self) -> None:
        """Clear the active framebuffer to black."""
        ...

    def CreateFrameCanvas(self) -> FrameCanvas:
        """Create an off-screen canvas for double or multi-buffering."""
        ...

    def SwapOnVSync(
        self,
        newFrame: FrameCanvas,
        framerate_fraction: int = 1,
    ) -> FrameCanvas:
        """Wait for VSync and swap in ``newFrame``.

        Returns the formerly active frame. ``framerate_fraction`` can slow
        animation to an exact integer fraction of the refresh rate.
        """
        ...

    @property
    def luminanceCorrect(self) -> bool:
        """Whether CIE1931 luminance correction is enabled."""
        ...

    @luminanceCorrect.setter
    def luminanceCorrect(self, luminanceCorrect: bool) -> None:
        """Enable or disable CIE1931 luminance correction."""
        ...

    @property
    def pwmBits(self) -> int:
        """PWM bit depth of the currently active frame."""
        ...

    @pwmBits.setter
    def pwmBits(self, pwmBits: int) -> None:
        """Set PWM bit depth for the active frame and future frames."""
        ...

    @property
    def brightness(self) -> int:
        """Matrix brightness percentage."""
        ...

    @brightness.setter
    def brightness(self, brightness: int) -> None:
        """Set brightness percentage for all created frames."""
        ...

    @property
    def height(self) -> int:
        """Matrix height in pixels."""
        ...

    @property
    def width(self) -> int:
        """Matrix width in pixels."""
        ...
