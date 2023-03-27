from bpy import types, props
from . import globals

class PA_AddonPrefs(types.AddonPreferences):
    bl_idname = __package__
    levelFolderPath: props.StringProperty(
        name="Level folder path",
        subtype="FILE_PATH",
        default="%programfiles(x86)%\\Steam\\steamapps\\common\\Project Arrhythmia\\beatmaps\\editor\\"
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="woo this is a test", icon_value=globals.custom_icons["pa_logo"].icon_id)
        layout.prop(self, "levelFolderPath")