# aaaaaaaaaaaaaaaaaaaaaaaa
from __future__ import annotations
from ..PAObject import PAObject

class PALevel():
    fullyLoaded: bool = False
    objects: dict[str, PAObject] = {}
    filepath: str = None

    audioFile: str = None

    def loadPreviewData(self, filepath: str):
        pass

    def loadFromFile(self, filepath: str, format: str = "vgd") -> PALevel:
        output = None
        # add try except after
        with open(filepath, "r") as f:
            output = self.loadFromString(f.read())
        
        self.filepath = filepath
        self.fullyLoaded = True
        return output


    def loadFromString(self, input: str, format: str = "vgd"):
        raise NotImplementedError()

class PALevelHandler():
    levels: list[PALevel]

    def __init__(self) -> None:
        pass