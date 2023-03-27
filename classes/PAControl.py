from bpy.types import Panel

class PA_PT_ContextControlPanel(Panel):
    bl_label = "Control Panel"
    bl_idname = "PA_PT_ContextControlPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Project Arrhythmia"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Yeet this is a test", icon="CUBE")