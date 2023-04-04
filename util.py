from __future__ import annotations
from bpy.types import Operator
from . import globals

def debug(message, op: Operator = None) -> None:
    if (globals.showDebug):
        print(f"PA [DEBUG] >> {message}\033[0m")
        if (op != None):
            op.report({ "DEBUG" }, message)

def info(message, op: Operator = None) -> None:
    print(f"PA [\033[96mINFO\033[0m]  >> {message}\033[0m")
    if (op != None):
        op.report({ "INFO" }, message)

def warn(message, op: Operator = None) -> None:
    print(f"PA [\033[93mWARN\033[0m]  >> {message}\033[0m")
    if (op != None):
        op.report({ "WARNING" }, message)

def error(message, op: Operator = None) -> None:
    print(f"PA [\033[91mERROR\033[0m] >> {message}\033[0m")
    if (op != None):
        op.report({ "ERROR" }, message)


class Colour():
    value: int = 0

    def getHex(self) -> str:
        return hex(self.value).removeprefix("0x").rjust(6, "0")
    
    def setHex(self, input) -> Colour:
        self.value = int(input, 16)
        return self
    
    def getRGB(self, maximum: int = 255) -> list[float]:
        return [((self.value & 0b1111_1111_0000_0000_0000_0000) >> 8 * 2) * (maximum / 255.0), ((self.value & 0b0000_0000_1111_1111_0000_0000) >> 8) * (maximum / 255.0), (self.value & 0b0000_0000_0000_0000_1111_1111) * (maximum / 255.0)]
    
    def setFromRGBArray(self, rgb: list[float], maximum: float = 255) -> Colour:
        self.setRGB(rgb[0], rgb[1], rgb[2], maximum=maximum)
        return self

    def setRGB(self, r: float = 0, g: float = 0, b: float = 0, maximum: float = 255) -> Colour:
        r = min(r, maximum)
        r /= maximum
        r = int(round(r * 255))

        g = min(g, maximum)
        g /= maximum
        g = int(round(g * 255))

        b = min(b, maximum)
        b /= maximum
        b = int(round(b * 255))

        r <<= 8 * 2
        g <<= 8

        self.value = r | g | b

        return self