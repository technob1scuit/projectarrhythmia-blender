from bpy.types import Operator
from ... import globals
from ...util import error

class PANewThemeOperator(Operator):
    bl_idname = "pa.new_theme"
    bl_label = "New theme"

    def execute(self, context):
        
        return { "FINISHED" }
    
class PARefreshThemeListOperator(Operator):
    bl_idname = "pa.refresh_theme_list"
    bl_label = "Refresh theme list"

    def execute(self, context):
        try:
            globals.themeHandler.loadThemes()
        except Exception as e:
            error(f"An error occured when attempting to reload the list of themes:\n{str(e)}", self)
        return { "FINISHED" }