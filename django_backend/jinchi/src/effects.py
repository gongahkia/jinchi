# ----- required imports -----

import time
import math
import random
import colorsys

# ----- class definitions -----


class TypewriterEffect:
    def __init__(self, text_obj):
        self.obj = text_obj
        self.visible_chars = 0

    def update(self, alpha):
        self.visible_chars = int(alpha * len(self.obj.text))
        self.obj.visible_text = self.obj.text[: self.visible_chars]


class FadeInEffect:
    def __init__(self, text_obj):
        self.obj = text_obj
        self.alpha = 0

    def update(self, alpha):
        self.alpha = int(alpha * 255)
        self.obj.alpha = self.alpha


class BlinkEffect:
    def __init__(self, text_obj, blink_rate=2):
        self.obj = text_obj
        self.blink_rate = blink_rate
        self.visible = True

    def update(self, alpha):
        time_sec = alpha * 2
        self.visible = (int(time_sec * self.blink_rate) % 2) == 0
        self.obj.visible = self.visible


class SlideInEffect:
    def __init__(self, text_obj, start_x, end_x):
        self.obj = text_obj
        self.start_x = start_x
        self.end_x = end_x

    def update(self, alpha):
        current_x = self.start_x + alpha * (self.end_x - self.start_x)
        self.obj.x = current_x


class ColorFadeEffect:
    def __init__(self, text_obj, start_color, end_color):
        self.obj = text_obj
        self.start_color = start_color
        self.end_color = end_color

    def update(self, alpha):
        r = int(self.start_color[0] + (self.end_color[0] - self.start_color[0]) * alpha)
        g = int(self.start_color[1] + (self.end_color[1] - self.start_color[1]) * alpha)
        b = int(self.start_color[2] + (self.end_color[2] - self.start_color[2]) * alpha)
        self.obj.color = (r, g, b)


class ScaleInEffect:
    def __init__(self, text_obj, start_scale=0.1, end_scale=1.0):
        self.obj = text_obj
        self.start_scale = start_scale
        self.end_scale = end_scale

    def update(self, alpha):
        self.obj.scale = self.start_scale + (self.end_scale - self.start_scale) * alpha


class RotateInEffect:
    def __init__(self, text_obj, start_angle=90):
        self.obj = text_obj
        self.start_angle = start_angle

    def update(self, alpha):
        self.obj.rotation = self.start_angle * (1 - alpha)


class DropInEffect:
    def __init__(self, text_obj, start_y, end_y):
        self.obj = text_obj
        self.start_y = start_y
        self.end_y = end_y

    def update(self, alpha):
        self.obj.y = self.start_y + (self.end_y - self.start_y) * alpha


class WaveEffect:
    def __init__(self, text_obj, amplitude=10, frequency=5):
        self.obj = text_obj
        self.amplitude = amplitude
        self.frequency = frequency

    def update(self, alpha):
        text = (
            self.obj.visible_text
            if hasattr(self.obj, "visible_text")
            else self.obj.text
        )
        offsets = []
        for i in range(len(text)):
            offset = self.amplitude * math.sin(
                2 * math.pi * self.frequency * (alpha + i / 10.0)
            )
            offsets.append(offset)
        self.obj.char_y_offsets = offsets


class JitterEffect:
    def __init__(self, text_obj, intensity=3):
        self.obj = text_obj
        self.intensity = intensity

    def update(self, alpha):
        self.obj.x_offset = random.randint(-self.intensity, self.intensity)
        self.obj.y_offset = random.randint(-self.intensity, self.intensity)


class ZoomOutEffect:
    def __init__(self, text_obj, start_scale=1.0, end_scale=0.1):
        self.obj = text_obj
        self.start_scale = start_scale
        self.end_scale = end_scale

    def update(self, alpha):
        self.obj.scale = self.start_scale + (self.end_scale - self.start_scale) * alpha
        self.obj.alpha = int(255 * (1 - alpha))


class UnderlineGrowEffect:
    def __init__(self, text_obj):
        self.obj = text_obj

    def update(self, alpha):
        self.obj.underline_length = int(len(self.obj.text) * alpha)


class LetterPopEffect:
    def __init__(self, text_obj):
        self.obj = text_obj

    def update(self, alpha):
        text = self.obj.text
        scales = []
        for i in range(len(text)):
            letter_alpha = min(max((alpha * len(text)) - i, 0), 1)
            scale = 0.5 + 0.5 * letter_alpha
            scales.append(scale)
        self.obj.char_scales = scales


class RainbowEffect:
    def __init__(self, text_obj):
        self.obj = text_obj

    def update(self, alpha):
        text = self.obj.text
        colors = []
        for i in range(len(text)):
            hue = (alpha + i / len(text)) % 1.0
            rgb = hsv_to_rgb(hue, 1, 1)
            colors.append(rgb)
        self.obj.char_colors = colors


# ----- helper functions -----


def hsv_to_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (int(r * 255), int(g * 255), int(b * 255))
