from __future__ import annotations
import bpy
import json as json
from ...globals import packageName
from random import randint
import os
from ...util import debug, error

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

    def readFromJSONObject(self, json: dict[str, any], format: str = "vgt") -> PATheme:
        self.themeData = {}

        print(type(bpy.context.preferences.addons[packageName].preferences.defaultGUIColour))

        if format == "lst":
            self.themeData["name"] = json["name"] or "Unnamed theme"
            self.themeData["gui"] = json["gui"]
            self.themeData["bg"] = json["bg"]
            self.themeData["id"] = json["id"] # isn't even in vgt themes lol
            for i in range(4):
                self.themeData["players"][i] = json["players"][i]
            for i in range(9):
                self.themeData["objects"][i] = json["objs"][i]
                self.themeData["bgObjects"][i] = json["bgs"][i]
        elif format == "vgt":
            self.themeData["name"] = json["name"]
            self.themeData["bg"] = json["base_bg"]
            self.themeData["gui"] = json["base_gui"]
            self.themeData["guiAccent"] = json["base_gui_accent"]
            for i in range(4):
                self.themeData["players"][i] = json["pla"][i]
            for i in range(9):
                self.themeData["objects"][i] = json["objs"][i]
                self.themeData["fx"][i] = json["fs"][i]
                self.themeData["bgObjects"][i] = json["bg"][i]
        else:
            print(f"what- what is a {format}...??")

        return self

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
            self.themeFolder = os.path.expandvars(bpy.context.preferences.addons[packageName].preferences.themeFolderPath)
        else:
            self.themeFolder = os.path.expandvars(customPath)
    
    def loadThemes(self) -> PAThemeHandler:
        self.loadedThemes = []

        allFilesInDir = [f for f in os.listdir(self.themeFolder) if os.path.isfile(os.path.join(self.themeFolder, f))]

        if (len(allFilesInDir) != 0):
            debug("Found following files in themes directory:")
            for f in allFilesInDir:
                debug(f)
        else:
            debug("No files found in themes directory.")
            return self

        lstThemes = [a for a in allFilesInDir if a.endswith(".lst")]
        vgtThemes = [a for a in allFilesInDir if a.endswith(".vgt")]
        
        debug(".lst themes found:")
        for t in lstThemes:
            debug(t)

        debug(".vgt themes found:")
        for t in vgtThemes:
            debug(t)
        
        unloadableThemes = []

        # load in lst themes
        for theme in lstThemes:
            try:
                themeObj = self.newTheme()

                content = ""
                with open(os.path.join(self.themeFolder, theme)) as f:
                    content = f.read()

                themeObj.readFromJSONString(content, format="lst")
            except Exception as e:
                error(f"Error loading lst theme {theme}:\n{str(e)}")
                unloadableThemes.append(theme)

        # load in vgt themes
        for theme in vgtThemes:
            try:
                themeObj = self.newTheme()

                content = ""
                with open(os.path.join(self.themeFolder, theme)) as f:
                    content = f.read()

                themeObj.readFromJSONString(content, format="vgt")
            except Exception as e:
                error(f"Error loading lst theme {theme}:\n{str(e)}")
                unloadableThemes.append(theme)

        return self

    def getAllThemes(self) -> list[PATheme]:
        return self.loadedThemes
    
    def newTheme(self) -> PATheme:
        theme = PATheme()
        self.loadedThemes.append(theme)
        return theme