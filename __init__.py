bl_info = {
    "name": "PA Editor",
    "description": "Implements an editor for Project Arrhythmia levels, prefabs and themes.",
    "author": "technobiscuit",
    "version": (0, 0, 1),
    "blender": (3, 5, 0),
    "location": "View3D > Project Arrhythmia",
    "warning": "This addon is still in HEAVY development - bugs are incredibly likely lol",
    "category": "3D View"
}

import sys
import os

# import modules
if "bpy" in locals():
    import importlib
    importlib.reload(util)
    importlib.reload(PA_PT_ContextControlPanel)
    importlib.reload(PA_AddonPrefs)
    importlib.reload(PA_PT_ThemePanel)
    importlib.reload(PA_PT_ThemeEditingPanel)
    importlib.reload(PANewThemeOperator)
else:
    print("projectarrhythmia >> attempting module imports")
    from . import util
    util.debug("Util functions imported successfully")

    from .classes.PAControl import PA_PT_ContextControlPanel
    from .configuration import PA_AddonPrefs
    from .classes.themes.PAThemePanel import PA_PT_ThemePanel, PA_PT_ThemeEditingPanel
    from .classes.themes.PAThemeOperators import PANewThemeOperator

    from .classes.themes.PAThemeHandler import PAThemeHandler

import bpy

classes = [
    PA_PT_ContextControlPanel,
    PA_AddonPrefs,
    PA_PT_ThemePanel,
    PA_PT_ThemeEditingPanel,
    PANewThemeOperator
]

from . import globals

def register():
    globals.init()

    globals.customIcons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    globals.customIcons.load("pa_logo", os.path.join(icons_dir, "pa_logo.png"), "IMAGE")

    util.debug("Registered icons")


    for cls in classes:
        bpy.utils.register_class(cls)


    globals.themeHandler = PAThemeHandler()
    
    globals.themeHandler.newTheme()

    test2 = globals.themeHandler.newTheme()
    test2.themeData["name"] = "this is a test"
    
    util.info("Registered successfully")

def unregister():
    global customIcons
    
    bpy.utils.previews.remove(globals.customIcons)
    util.debug("Unregistered icons")
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    util.info("Unregistered successfully")

if __name__ == "__main__":
    register()