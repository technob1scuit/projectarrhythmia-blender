from __future__ import annotations
import bpy
import json as json
from ... import globals
from random import randint
import os
from ...util import debug, info, error, Colour
from ... import png

themeIconFolder: str = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons", globals.packageName, "themeIcons")

class PATheme():
    filePath: str
    themeData: dict[str, any] = None
    savedToDisk: bool = False
    iconValue = None
    iconPath: str = None

    scenePropertyIndex: int = None

    iconFolder: str = themeIconFolder

    def __init__(self) -> None:
        prefs = bpy.context.preferences.addons[globals.packageName].preferences

        self.themeData = {
            "name": "Unnamed theme",
            "id": randint(10000, 999999), # i have no idea what the limits are for the id lol
            "gui": Colour().setFromRGBArray(prefs.defaultGUIColour, maximum=1.0),
            "guiAccent": Colour().setFromRGBArray(prefs.defaultGUIAccentColour, maximum=1.0),
            "bg": Colour().setFromRGBArray(prefs.defaultBGColour, maximum=1.0),
            "players": [
                Colour().setFromRGBArray(prefs.defaultPlayerOneColour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultPlayerTwoColour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultPlayerThreeColour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultPlayerFourColour, maximum=1.0)
            ],
            "objects": [
                Colour().setFromRGBArray(prefs.defaultObject0Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject1Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject2Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject3Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject4Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject5Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject6Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject7Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultObject8Colour, maximum=1.0)
            ],
            "fx": [
                Colour().setFromRGBArray(prefs.defaultEffect0Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect1Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect2Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect3Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect4Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect5Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect6Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect7Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultEffect8Colour, maximum=1.0)
            ],
            "bgObjects": [
                Colour().setFromRGBArray(prefs.defaultParallax0Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax1Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax2Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax3Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax4Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax5Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax6Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax7Colour, maximum=1.0),
                Colour().setFromRGBArray(prefs.defaultParallax8Colour, maximum=1.0)
            ]
        }

    def generateIcon(self, name: str = None, force: bool = False) -> PATheme:
        fileName = name if name != None else f"{randint(0, 9999999)}.png"
        filepath = os.path.join(self.iconFolder, fileName)
        if os.path.exists(filepath) == False or force == True:
            colours: list[Colour] = self.themeData["objects"]
            rgbValues = [[int(round(a.getRGB()[0])), int(round(a.getRGB()[1])), int(round(a.getRGB()[2]))] for a in colours]
            row = []
            for i in range (9):
                for x in range(3 if i % 2 == 1 else 4):
                    for c in range(3):
                        row.append(rgbValues[i][c])

            rowT = tuple(row)
            icon = []
            for i in range(32):
                icon.append(rowT)
            png.from_array(icon, mode="RGB").save(filepath)

        self.setIcon(fileName, filepath)
        return self
    
    def setIcon(self, name: str = None, path: str = None) -> PATheme:
        if name == None: name = self.themeData["name"]
        if path == None: path = os.path.join(self.iconFolder, name)

        globals.themeIcons.load(f"pa_theme_{name}", os.path.join(path), "IMAGE")

        self.iconValue = globals.themeIcons[f"pa_theme_{name}"].icon_id
        
        bpy.context.scene.themes[self.scenePropertyIndex].iconValue = self.iconValue

        return self
    
    def updateFromEditorValues(self, properties) -> PATheme:
        self.themeData["name"] = properties.name
        self.the

    def resetToDefaults(self) -> PATheme:
        self.themeData = PATheme().themeData
        return self

    def readFromJSONString(self, inJson: str, format: str = "vgt") -> PATheme:
        return self.readFromJSONObject(json.loads(inJson), format)

    def readFromJSONObject(self, json: dict[str, any], format: str = "vgt") -> PATheme:
        self.resetToDefaults()

        if format == "lst":
            self.themeData["name"] = json["name"] or "Unnamed theme"
            self.themeData["gui"] = Colour().setHex(json["gui"] or "000000")
            self.themeData["bg"] = Colour().setHex(json["bg"] or "000000")
            self.themeData["id"] = json["id"] or randint(10000, 999999) # isn't even in vgt themes lol
            for i in range(4):
                self.themeData["players"][i] = Colour().setHex(json["players"][i])
            for i in range(9):
                self.themeData["objects"][i] = Colour().setHex(json["objs"][i] if json["objs"] != None else "000000")
                self.themeData["bgObjects"][i] = Colour().setHex(json["bgs"][i] if json["bgs"] != None else "000000")
        elif format == "vgt":
            self.themeData["name"] = json["name"]
            self.themeData["bg"] = Colour().setHex(json["base_bg"])
            self.themeData["gui"] = Colour().setHex(json["base_gui"])
            self.themeData["guiAccent"] = Colour().setHex(json["base_gui_accent"])
            for i in range(4):
                self.themeData["players"][i] = Colour().setHex(json["pla"][i])
            for i in range(9):
                self.themeData["objects"][i] = Colour().setHex(json["obj"][i] if json["obj"] != None else "000000")
                self.themeData["fx"][i] = Colour().setHex(json["fx"][i] if json["fx"] != None else "000000")
                self.themeData["bgObjects"][i] = Colour().setHex(json["bg"][i] if json["bg"] != None else "000000")
        else:
            print(f"what- what is a {format}...??")

        bpy.context.scene.themes[self.scenePropertyIndex].name = self.themeData["name"]

        return self

    def toLSTString(self) -> str:
        outputTheme = {
            "id": self.themeData["id"],
            "name": self.themeData["name"],
            "gui": self.themeData["gui"].getHex().upper(),
            "bg": self.themeData["bg"].getHex().upper(),
            "players": [a.getHex().upper() for a in self.themeData["players"]],
            "objs": [a.getHex().upper() for a in self.themeData["objects"]],
            "bgs": [a.getHex().upper() for a in self.themeData["bgObjects"]]
        }

        return json.dumps(outputTheme, separators=(',', ':'))
    
    def toVGTString(self) -> str:
        outputTheme = {
            "name": self.themeData["name"],
            "pla": [a.getHex().upper() for a in self.themeData["players"]],
            "obj": [a.getHex().upper() for a in self.themeData["objects"]],
            "fx": [a.getHex().upper() for a in self.themeData["fx"]],
            "bg": [a.getHex().upper() for a in self.themeData["bgObjects"]],
            "base_bg": self.themeData["bg"].getHex().upper(),
            "base_gui": self.themeData["gui"].getHex().upper(),
            "base_gui_accent": self.themeData["guiAccent"].getHex().upper()
        }

        return json.dumps(outputTheme, separators=(',', ':'))

class PAThemeHandler():
    themeFolder: str
    loadedThemes: list[PATheme] = []

    firstLoadComplete: bool = False

    def __init__(self, customPath: str = None) -> None:
        if (customPath == None):
            self.themeFolder = os.path.expandvars(bpy.context.preferences.addons[globals.packageName].preferences.themeFolderPath)
        else:
            self.themeFolder = os.path.expandvars(customPath)

    def loadThemes(self) -> PAThemeHandler:
        self.loadedThemes = []

        allFilesInDir = [f for f in os.listdir(self.themeFolder) if os.path.isfile(os.path.join(self.themeFolder, f))]

        if (len(allFilesInDir) != 0):
            debug("Found following files in themes directory:")
            for f in allFilesInDir:
                debug(f"\t- {f}")
        else:
            debug("No files found in themes directory.")
            return self

        lstThemes = [a for a in allFilesInDir if a.endswith(".lst")]
        vgtThemes = [a for a in allFilesInDir if a.endswith(".vgt")]
        
        debug(".lst themes found:")
        for t in lstThemes:
            debug(f"\t- {t}")

        debug(".vgt themes found:")
        for t in vgtThemes:
            debug(f"\t- {t}")
        
        unloadableThemes = []

        # load in lst themes
        for theme in lstThemes:
            try:
                themeObj = self.newTheme()

                content = ""
                with open(os.path.join(self.themeFolder, theme)) as f:
                    content = f.read()

                themeObj.savedToDisk = True
                themeObj.readFromJSONString(content, format="lst")
                themeObj.generateIcon(os.path.splitext(theme)[0] + ".png")
                debug(f"Loaded {theme}.")
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

                themeObj.savedToDisk = True
                themeObj.readFromJSONString(content, format="vgt")
                themeObj.generateIcon(os.path.splitext(theme)[0] + ".png")
                debug(f"Loaded {theme}.")
            except Exception as e:
                error(f"Error loading vgt theme {theme}:\n{str(e)}")
                unloadableThemes.append(theme)

        info("Finished loading themes.")
        return self

    def getAllThemes(self) -> list[PATheme]:
        return self.loadedThemes
    
    def newTheme(self) -> PATheme:
        theme = PATheme()
        self.loadedThemes.append(theme)

        item = bpy.context.scene.themes.add()
        item.name = theme.themeData["name"]
        item.loadedThemesIndex = len(self.loadedThemes) - 1
        theme.scenePropertyIndex = len(bpy.context.scene.themes) - 1

        return theme
    
if __name__ == "__main__":
    PATheme().generateIcon("test")