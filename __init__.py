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
    importlib.reload(PARefreshThemeListOperator)
else:
    print("projectarrhythmia >> attempting module imports")
    from . import util
    util.debug("Util functions imported successfully")

    from .classes.PAControl import PA_PT_ContextControlPanel
    from .configuration import PA_AddonPrefs
    from .classes.themes.PAThemePanel import PA_PT_ThemePanel, PA_PT_ThemeEditingPanel
    from .classes.themes.PAThemeOperators import PANewThemeOperator, PARefreshThemeListOperator

    from .classes.themes.PAThemeHandler import PAThemeHandler

import bpy

classes = [
    PA_PT_ContextControlPanel,
    PA_AddonPrefs,
    PA_PT_ThemePanel,
    PA_PT_ThemeEditingPanel,
    PANewThemeOperator,
    PARefreshThemeListOperator
]

from . import globals

def register():
    globals.init()

    globals.customIcons = bpy.utils.previews.new()
    globals.themeIcons = bpy.utils.previews.new()

    iconsDir = os.path.join(os.path.dirname(__file__), "icons")

    globals.customIcons.load("pa_logo", os.path.join(iconsDir, "pa_logo.png"), "IMAGE")

    util.debug("Registered icons")


    for cls in classes:
        bpy.utils.register_class(cls)

    util.info("Registered successfully")

    globals.themeHandler = PAThemeHandler()

    util.info("Loading themes...")
    globals.themeHandler.loadThemes()
    

def unregister():
    global customIcons
    
    bpy.utils.previews.remove(globals.customIcons)
    bpy.utils.previews.remove(globals.themeIcons)

    util.debug("Unregistered icons")
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    util.info("Unregistered successfully")

if __name__ == "__main__":
    register()