import os.path

from PIL import Image, ImageDraw, ImageFont, ImageQt

from PySide6.QtGui import QIcon, QPixmap

import math
from numpy import random

from typing import Optional


class Gradients:
    __gradients = [
        ["00ff87", "60efff"],
        ["0061ff", "60efff"],
        ["ff1b6b", "45caff"],
        ["40c9ff", "e81cff"],
        ["ff930f", "fff95b"],
        ["696eff", "f8acff"],
        ["1dbde6", "f1515e"],
        ["b2ef91", "fa9372"],
        ["b429f9", "26c5f3"],
        ["ff5858", "ffc8c8"],
    ]

    @staticmethod
    def __from_hex_to_rgb(__hex_color: str) -> tuple:
        return tuple(int(__hex_color[i:i + 2], 16) for i in (0, 2, 4))

    @classmethod
    def get_random_gradient(cls, __type: str = "rgb") -> list:
        if __type.lower() == "rgb":
            return list(map(cls.__from_hex_to_rgb, cls.__gradients[random.randint(0, len(cls.__gradients))]))

        elif __type.lower() == "hex":
            return cls.__gradients[random.randint(0, len(cls.__gradients))]


class ProjectNameGenerator:
    @staticmethod
    def __upper_letters(__string: str) -> Optional[str]:
        uppers = []

        for char in __string:
            if char.isupper(): uppers.append(char)

        match len(uppers):
            case upp if upp in (1, 2):
                return "".join(uppers)

            case upp if upp > 2:
                return "".join(uppers[:2])

            case _: return None

    @staticmethod
    def __spliter(__string: str) -> Optional[str]:
        splitter_symbols = "_ -/\\|"
        res = []

        for symbol in splitter_symbols:
            dist = __string.split(symbol)

            if len(dist) >= 2:
                res.append("".join([i[0] for i in dist[:2]]))

        return res[0].upper() if len(res) > 0 else None

    @staticmethod
    def __first_letter(__string: str) -> str:
        for char in __string:
            if char.isalpha(): return char.upper()

        return __string[0].upper()

    @classmethod
    def get_basename(cls, __name: str) -> str:
        result = list(filter(lambda x: x != None, [cls.__upper_letters(__name), cls.__spliter(__name)]))

        if len(result) != 0: return result[0]
        else: return cls.__first_letter(__name)


class ImageGenerator:

    @classmethod
    def __diagonal_gradient(
            cls, __image: Image.Image,
            __from: tuple[int, int, int], __to: tuple[int, int, int]
    ) -> Image.Image:
        start_x, start_y = 0, 0

        pixel_data = __image.load()

        for x in range(__image.size[0]):
            for y in range(__image.size[1]):
                dist = math.fabs(start_x - x) + math.fabs(start_y - y)
                dist = dist / (__image.size[0] + __image.size[1])

                r, g, b = map(
                    lambda start, end: start + end,
                    map(lambda start: start * (1 - dist), __from),
                    map(lambda end: end * dist, __to)
                )

                pixel_data[x, y] = int(r), int(g), int(b)

        return __image

    @classmethod
    def __round_corners(cls, __image: Image.Image, __radius: int) -> Image.Image:
        circle = Image.new('L', (__radius * 2, __radius * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, __radius * 2 - 1, __radius * 2 - 1), fill=255)
        alpha = Image.new('L', __image.size, 255)

        w, h = __image.size

        alpha.paste(circle.crop((0, 0, __radius, __radius)), (0, 0))
        alpha.paste(circle.crop((0, __radius, __radius, __radius * 2)), (0, h - __radius))
        alpha.paste(circle.crop((__radius, 0, __radius * 2, __radius)), (w - __radius, 0))
        alpha.paste(circle.crop((__radius, __radius, __radius * 2, __radius * 2)), (w - __radius, h - __radius))

        __image.putalpha(alpha)

        return __image

    @classmethod
    def __add_text(cls, __image: Image.Image, __text: str) -> Image.Image:
        draw = ImageDraw.Draw(__image)

        font = ImageFont.truetype("assets/fonts/CascadiaMono.ttf", 200)

        (width, baseline), (offset_x, offset_y) = font.font.getsize(__text)
        x = (__image.width - width - offset_x * 1.5) // 2
        y = (__image.height - baseline - offset_y * 1.5) // 2

        # Draw the text
        draw.text((x, y), __text, font=font, fill="white")

        return __image.copy()

    @classmethod
    def generate(cls, __size: tuple[int, int], __text: str) -> Image.Image:
        __image = Image.new('RGB', __size)

        __image = cls.__diagonal_gradient(__image, *Gradients.get_random_gradient())
        __image = cls.__round_corners(__image, 50)
        __image = cls.__add_text(__image, __text)

        return __image

    @staticmethod
    def save(__name: str, __image: Image.Image) -> str:
        __path = os.path.join("assets\\project_icons", __name + ".png")
        __image.save(__path)

        return __path

    @classmethod
    def to_qicon(cls, __image: Image.Image) -> QIcon:
        qimage = ImageQt.ImageQt(__image)

        return QIcon(QPixmap.fromImage(qimage))
