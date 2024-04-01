import random


class Gradients:
    __gradients = [
        ["00ff87", "60efff"],["0061ff", "60efff"],["ff1b6b", "45caff"],["40c9ff", "e81cff"],["ff930f", "fff95b"],
        ["696eff", "f8acff"],["1dbde6", "f1515e"],["b2ef91", "fa9372"],["b429f9", "26c5f3"],["ff5858", "ffc8c8"],
        ["00ff87", "60efff"],["0061ff", "60efff"],["ff1b6b", "45caff"],["40c9ff", "e81cff"],["ff930f", "fff95b"],
        ["696eff", "f8acff"],["1dbde6", "f1515e"],["b2ef91", "fa9372"],["b429f9", "26c5f3"],["ff5858", "ffc8c8"],
        ["ff7f00", "ffcc00"],["ff6666", "ff99cc"],["33ccff", "99ccff"],["ff3399", "ff99cc"],["66ccff", "ccffff"],
        ["ffcc00", "ffff66"],["ff6699", "ff99cc"],["3399ff", "66ccff"],["ff6666", "ffcccc"],["66ccff", "99ccff"],
        ["ffcc00", "ffcc66"],["ff6666", "ff9999"],["33ccff", "66ccff"],["ff3399", "ff6699"],["66ccff", "99ccff"],
        ["ffcc00", "ffcc33"],["ff6666", "ff6666"],["33ccff", "66ccff"],["ff3399", "ff3399"],["66ccff", "99ccff"],
        ["ffcc00", "ffcc00"],["ff6666", "ff6666"],["33ccff", "66ccff"],["ff3399", "ff3399"],["66ccff", "99ccff"],
        ["ffcc00", "ffcc00"],["ff6666", "ff6666"],["33ccff", "66ccff"],["ff3399", "ff3399"],["66ccff", "99ccff"],
        ["ffcc00", "ffcc00"],["ff6666", "ff6666"],["33ccff", "66ccff"],["ff3399", "ff3399"],["66ccff", "99ccff"],
        ["ffcc00", "ffcc00"],["ff6666", "ff6666"],["33ccff", "66ccff"],["ff3399", "ff3399"],["66ccff", "99ccff"]
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