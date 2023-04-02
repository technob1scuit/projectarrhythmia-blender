from __future__ import annotations
import bpy
import json as json
from ...globals import packageName
from random import randint

class PATheme():
    filePath: str
    themeData: dict[str, any] = None
    savedToDisk: bool = False

    def __init__(self) -> None:
        self.themeData = {
            "name": "Unnamed theme",
            "id": randint(10000, 999999), # i have no idea what the limits are for the id lol
            "gui": bpy.context.preferences.addons[packageName].preferences.defaultGUIColour,
            "guiAccent": bpy.context.preferences.addons[packageName].preferences.defaultGUIAccentColour,
            "bg": bpy.context.preferences.addons[packageName].preferences.defaultBGColour,
            "players": [
                bpy.context.preferences.addons[packageName].preferences.defaultPlayerOneColour,
                bpy.context.preferences.addons[packageName].preferences.defaultPlayerTwoColour,
                bpy.context.preferences.addons[packageName].preferences.defaultPlayerThreeColour,
                bpy.context.preferences.addons[packageName].preferences.defaultPlayerFourColour
            ],
            "objects": [
                bpy.context.preferences.addons[packageName].preferences.defaultObject0Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject1Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject2Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject3Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject4Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject5Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject6Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject7Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultObject8Colour
            ],
            "fx": [
                bpy.context.preferences.addons[packageName].preferences.defaultEffect0Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect1Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect2Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect3Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect4Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect5Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect6Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect7Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultEffect8Colour
            ],
            "bgObjects": [
                bpy.context.preferences.addons[packageName].preferences.defaultParallax0Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax1Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax2Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax3Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax4Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax5Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax6Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax7Colour,
                bpy.context.preferences.addons[packageName].preferences.defaultParallax8Colour
            ]
        }

    def readFromJSONString(self, inJson: str, format: str = "vgt") -> PATheme:
        return self.readFromJSONObject(json.loads(inJson), format)

    def readFromJSONObject(self, json: dict[str, any], format: str = "vgt"):
        raise NotImplementedError()

    def toLSTString(self) -> str:
        outputTheme = {
            "id": self.themeData["id"],
            "name": self.themeData["name"],
            "gui": self.themeData["gui"],
            "bg": self.themeData["bg"],
            "players": self.themeData["players"],
            "objs": self.themedata["objects"],
            "bgs": self.themeData["bgObjects"]
        }

        return json.dumps(outputTheme)
    
    def toVGTString(self) -> str:
        outputTheme = {
            "name": self.themeData["name"],
            "pla": self.themeData["players"],
            "obj": self.themeData["objects"],
            "fx": self.themeData["fx"],
            "bg": self.themeData["bgObjects"],
            "base_bg": self.themeData["bg"],
            "base_gui": self.themeData["gui"],
            "base_gui_accent": self.themeData["guiAccent"]
        }

        return json.dumps(outputTheme)

class PAThemeHandler():
    themeFolder: str
    loadedThemes: list[PATheme] = []

    def __init__(self, customPath: str = None) -> None:
        if (customPath == None):
            self.themeFolder = bpy.context.preferences.addons[packageName].preferences.themeFolderPath
        else:
            self.themeFolder = customPath

    def getAllThemes() -> list[PATheme]:
        raise NotImplementedError()
    
    def newTheme(self) -> PATheme:
        theme = PATheme()
        self.loadedThemes.append(theme)
        return theme