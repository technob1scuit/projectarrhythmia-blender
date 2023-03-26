bl_info = {
    "name": "PA Editor",
    "description": "Implements an editor for Project Arrhythmia levels, prefabs and themes.",
    "author": "technobiscuit",
    "version": (0, 0, 1),
    "blender": (3, 4, 0),
    "location": "somewhere",
    "warning": "This addon is still in HEAVY development - bugs are incredibly likely lol",
    "category": "this deserves its own category"
}

import bpy

classes = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()