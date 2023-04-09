from bpy.types import Panel, UIList

import bpy
from ... import globals

class PA_PT_LevelPanel(Panel):
    bl_label = "Levels"
    bl_idname = "PA_PT_LevelPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Project Arrhythmia"

    def draw(self, context) -> None:
        layout = self.layout

        layout.label(text="this will happen later")