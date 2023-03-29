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
else:
    print("projectarrhythmia >> attempting module imports")
    from . import util
    util.debug("Util functions imported successfully")

    from .classes.PAControl import PA_PT_ContextControlPanel
    from .configuration import PA_AddonPrefs

import bpy

imports = []

classes = [
    PA_PT_ContextControlPanel,
    PA_AddonPrefs
]

from . import globals

def register():
    globals.init()
    globals.custom_icons = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    globals.custom_icons.load("pa_logo", os.path.join(icons_dir, "pa_logo.png"), "IMAGE")

    util.debug("Registered icons")

    for cls in classes:
        bpy.utils.register_class(cls)
    
    util.info("Registered successfully")

def unregister():
    bpy.utils.previews.remove(globals.custom_icons)
    util.debug("Unregistered icons")
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    util.info("Unregistered successfully")

if __name__ == "__main__":
    register()