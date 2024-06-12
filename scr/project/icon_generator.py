import math
import os.path
from typing import Optional

from PIL import Image, ImageDraw, ImageFont, ImageQt
from PySide6.QtGui import QIcon, QPixmap

from scr.resources.colors import Gradients


class ProjectNameGenerator:
    @staticmethod
    def __upper_letters(__string: str) -> Optional[str]:
        """
        Extracts uppercase letters from a string based on specific conditions.

        Parameters:
        __string (str): The input string to extract uppercase letters from.

        Returns:
        Optional[str]: Extracted uppercase letters or None.
        """

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
        """
        Splits a string based on predefined symbols and returns a formatted result.

        Parameters:
        __string (str): The input string to split.

        Returns:
        Optional[str]: Formatted string after splitting or None.
        """

        splitter_symbols = "_ -/\\|"
        res = []

        for symbol in splitter_symbols:
            dist = __string.split(symbol)

            if len(dist) >= 2:
                res.append("".join([i[0] for i in dist[:2]]))

        return res[0].upper() if len(res) > 0 else None

    @staticmethod
    def __first_letter(__string: str) -> str:
        """
        Retrieves the first alphabetic character from a string.

        Parameters:
        __string (str): The input string to extract the first letter from.

        Returns:
        str: The first uppercase letter from the input string.
        """

        for char in __string:
            if char.isalpha(): return char.upper()

        return __string[0].upper()

    @classmethod
    def get_basename(cls, __name: str) -> str:
        """
        Generates a basename for a given name by combining results from other methods.

        Parameters:
        __name (str): The input name to generate a basename for.

        Returns:
        str: The generated basename for the input name.
        """

        result = list(filter(lambda x: x != None, [cls.__upper_letters(__name), cls.__spliter(__name)]))

        if len(result) != 0: return result[0]
        else: return cls.__first_letter(__name)


class ImageGenerator:

    @classmethod
    def __diagonal_gradient(
            cls, __image: Image.Image,
            __from: tuple[int, int, int], __to: tuple[int, int, int]
    ) -> Image.Image:
        """
        Creates a diagonal gradient on an image from one color to another.

        Parameters:
        __image (Image.Image): The input image to apply the gradient to.
        __from (tuple[int, int, int]): RGB values for the starting color.
        __to (tuple[int, int, int]): RGB values for the ending color.

        Returns:
        Image.Image: Image with the applied diagonal gradient.
        """

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
        """
        Rounds the corners of an image with a specified radius.

        Parameters:
        __image (Image.Image): The input image to round the corners of.
        __radius (int): The radius for rounding the corners.

        Returns:
        Image.Image: Image with rounded corners.
        """

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
        """
        Adds text to an image at the center with a specified font.

        Parameters:
        __image (Image.Image): The input image to add text to.
        __text (str): The text to be added to the image.

        Returns:
        Image.Image: Image with the added text.
        """

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
        """
        Generates an image with a diagonal gradient, rounded corners, and added text.

        Parameters:
        __size (tuple[int, int]): Size of the generated image.
        __text (str): Text to be added to the image.

        Returns:
        Image.Image: The generated image.
        """

        __image = Image.new('RGB', __size)

        __image = cls.__diagonal_gradient(__image, *Gradients.get_random_gradient())
        __image = cls.__round_corners(__image, 50)
        __image = cls.__add_text(__image, __text)

        return __image

    @staticmethod
    def save(__name: str, __image: Image.Image) -> str:
        """
        Saves the generated image to a specified path.

        Parameters:
        __name (str): The name to be used for the saved image.
        __image (Image.Image): The image to be saved.

        Returns:
        str: The path where the image is saved.
        """

        __path = os.path.join("assets\\project_icons", __name + ".png")
        __image.save(__path)

        return __path

    @classmethod
    def to_qicon(cls, __image: Image.Image) -> QIcon:
        """
        Converts an Image.Image to a QIcon for Qt applications.

        Parameters:
        __image (Image.Image): The image to be converted to QIcon.

        Returns:
        QIcon: The converted QIcon.
        """

        qimage = ImageQt.ImageQt(__image)

        return QIcon(QPixmap.fromImage(qimage))
