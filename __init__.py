bl_info = {
    "name": "PA Editor",
    "description": "Implements an editor for Project Arrhythmia levels, prefabs and themes.",
    "author": "technobiscuit",
    "version": (0, 0, 1),
    "blender": (3, 4, 0),
    "location": "somewhere",
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
else:
    print("projectarrhythmia >> attempting module imports")
    from . import util
    util.debug("Util functions imported successfully")

    from .classes.PAControl import PA_PT_ContextControlPanel

import bpy

imports = []

classes = [
    PA_PT_ContextControlPanel
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()