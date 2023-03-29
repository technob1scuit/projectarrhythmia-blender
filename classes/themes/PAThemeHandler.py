from __future__ import annotations
import bpy
import json as json

class PATheme():
    filePath: str
    themeData: dict[str, any] = None

    def __init__(self) -> None:
        self.themeData = {
            "name": "Unnamed theme",
            "gui": "ABCDEF",
            "bg": "212121",
            "players": [
                bpy.context.preferences.addons[__package__].preferences.defaultPlayerOneColour,
                bpy.context.preferences.addons[__package__].preferences.defaultPlayerTwoColour,
                bpy.context.preferences.addons[__package__].preferences.defaultPlayerThreeColour,
                bpy.context.preferences.addons[__package__].preferences.defaultPlayerFourColour
            ]
        }

    def readFromJSONString(self, inJson: str) -> PATheme:
        return self.readFromJSONObject(json.loads(inJson))

    def readFromJSONObject(self, json: dict[str, any]):
        raise NotImplementedError()

    def toLSTString(self) -> str:
        raise NotImplementedError()
    
    def toVGTString(self) -> str:
        raise NotImplementedError()

class PAThemeHandler():
    themeFolder: str

    def __init__(self, customPath: str) -> None:
        if (customPath == None):
            self.themeFolder = bpy.context.preferences.addons[__package__].preferences.themeFolderPath
        else:
            self.themeFolder = customPath

    def getAllThemes() -> list[PATheme]:
        raise NotImplementedError()
