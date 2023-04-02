from bpy.types import Operator
from ...globals import themeHandler

class PANewThemeOperator(Operator):
    bl_idname = "pa.new_theme"
    bl_label = "New theme"

    def execute(self, context):
        
        return { "FINISHED" }