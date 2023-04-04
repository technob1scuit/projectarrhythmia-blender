from bpy.types import Panel, UILayout
from .PAThemeHandler import PATheme, PAThemeHandler
from ... import globals

class PA_PT_ThemePanel(Panel):
    bl_label = "PA Themes"
    bl_idname = "PA_PT_ThemePanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Project Arrhythmia"
    bl_options = { "DEFAULT_CLOSED" }

    def draw(self, context) -> None:
        layout = self.layout

        layout.operator("pa.refresh_theme_list", icon="FILE_REFRESH")

        self.drawThemeList(layout)

    def drawThemeList(self, layout: UILayout) -> None:
        themeHandler: PAThemeHandler = globals.themeHandler
        themes = themeHandler.loadedThemes

        # themes.append(PATheme())

        if len(themes) == 0:
            layout.label(text="No themes found! Either create a new one or change the theme file path in the addon's settings.", icon="ERROR")
        else:
            for i in range(len(themes)):
                row = layout.row()
                row.label(icon_value=themes[i].iconValue)
                row.label(text=themes[i].themeData["name"])


class PA_PT_ThemeEditingPanel(Panel):
    bl_category = "Project Arrhythmia"
    bl_idname = "PA_PT_ThemeEditingPanel"
    bl_parent_id = "PA_PT_ThemePanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Theme Editor"
    bl_options = { "DEFAULT_CLOSED" }

    def draw(self, context) -> None:
        layout = self.layout

        layout.label(text="woo this is a test")