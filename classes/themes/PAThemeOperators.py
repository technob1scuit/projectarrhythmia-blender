from bpy.types import Operator
from bpy.props import StringProperty
from bpy_extras.io_utils import ExportHelper
from ... import globals
from ...util import error, info, debug

class PA_OT_SaveSelectedThemeAsLSTOperator(Operator, ExportHelper):
    bl_idname = "pa.save_selected_lst"
    bl_label = "Save as .lst"
    bl_description = "Save the currently selected theme as an LST file."

    filename_ext = ".lst"

    filter_glob: StringProperty(
        default="*.lst",
        options={ "HIDDEN" },
        maxlen=255
    )

    def execute(self, context):
        scn = context.scene
        selectedThemePropertyGroup = scn.themes[scn.themePanelSelectedTheme]
        if scn.themePanelSelectedTheme < 0 or scn.themePanelSelectedTheme >= len(globals.themeHandler.loadedThemes):
            return { "CANCELLED" }
    
        selectedTheme = globals.themeHandler.loadedThemes[selectedThemePropertyGroup.loadedThemesIndex]
        
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(selectedTheme.toLSTString())

        selectedTheme.savedToDisk = True
        return { "FINISHED" }
    
class PA_OT_SaveSelectedThemeAsVGTOperator(Operator, ExportHelper):
    bl_idname = "pa.save_selected_vgt"
    bl_label = "Save as .vgt"
    bl_description = "Save the currently selected theme as a VGT file."

    filename_ext = ".vgt"

    filter_glob: StringProperty(
        default="*.vgt",
        options={ "HIDDEN" },
        maxlen=255
    )

    def execute(self, context):
        scn = context.scene
        selectedThemePropertyGroup = scn.themes[scn.themePanelSelectedTheme]
        if scn.themePanelSelectedTheme < 0 or scn.themePanelSelectedTheme >= len(globals.themeHandler.loadedThemes):
            return { "CANCELLED" }
    
        selectedTheme = globals.themeHandler.loadedThemes[selectedThemePropertyGroup.loadedThemesIndex]
        
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(selectedTheme.toVGTString())
            
        selectedTheme.savedToDisk = True
        return { "FINISHED" }

class PA_OT_NewThemeOperator(Operator):
    bl_idname = "pa.new_theme"
    bl_label = "New theme"
    bl_description = "Add a new theme. This does not save the new theme to the disk"

    def execute(self, context):
        globals.themeHandler.newTheme()
        return { "FINISHED" }
    
class PA_OT_DeleteSelectedThemeOperator(Operator):
    bl_idname = "pa.delete_selected_theme"
    bl_label = "Delete selected theme"
    bl_description = "Remove the selected theme from the display. (this may delete the theme file in the future if people want it to do that)"

    def execute(self, context):
        scn = context.scene
        if scn.themePanelSelectedTheme < 0 or scn.themePanelSelectedTheme >= len(globals.themeHandler.loadedThemes):
            return { "CANCELLED" }

        themeToDelete = scn.themes[scn.themePanelSelectedTheme]
        themeIndex = themeToDelete.loadedThemesIndex

        del globals.themeHandler.loadedThemes[themeIndex]
        scn.themes.remove(scn.themePanelSelectedTheme)


        return { "FINISHED" }
    
class PA_OT_RefreshThemeListOperator(Operator):
    bl_idname = "pa.refresh_theme_list"
    bl_label = "Refresh theme list"
    bl_description = "Refresh the list of loaded themes using theme files saved in the themes folder"

    def execute(self, context):
        try:
            globals.themeHandler.loadThemes()
            # forces theme editor to refresh
            context.scene.themePanelSelectedTheme += 1
            context.scene.themePanelSelectedTheme -= 1
        except Exception as e:
            error(f"An error occured when attempting to reload the list of themes:\n{str(e)}", self)
        return { "FINISHED" }