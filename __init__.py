bl_info = {
    "name": "PA Editor",
    "description": "Implements an editor for Project Arrhythmia levels, prefabs and themes.",
    "author": "technobiscuit",
    "version": (0, 0, 2),
    "blender": (3, 5, 0),
    "location": "View3D > Project Arrhythmia",
    "warning": "This addon is still in HEAVY development - bugs are incredibly likely lol",
    "category": "3D View"
}

import os

# import modules
if "bpy" in locals():
    import importlib
    importlib.reload(util)
    importlib.reload(PA_PT_ContextControlPanel)

    importlib.reload(PA_AddonPrefs)

    importlib.reload(PA_PT_ThemePanel)
    importlib.reload(PA_PT_ThemeEditingPanel)
    importlib.reload(PA_PT_ThemeEditing_PlayerPanel)
    importlib.reload(PA_PG_ThemeEditorValues)
    importlib.reload(ThemeEditor_SelectedThemeChange)
    importlib.reload(PA_PT_ThemeEditing_ObjectPanel)
    importlib.reload(PA_PT_ThemeEditing_BackgroundObjectPanel)
    importlib.reload(PA_PT_ThemeEditing_FXPanel)

    importlib.reload(PA_OT_NewThemeOperator)
    importlib.reload(PA_OT_RefreshThemeListOperator)
    importlib.reload(PA_OT_DeleteSelectedThemeOperator)
    importlib.reload(PA_OT_SaveSelectedThemeAsLSTOperator)
    importlib.reload(PA_OT_SaveSelectedThemeAsVGTOperator)

    importlib.reload(PA_UL_ThemeList)
else:
    print("projectarrhythmia >> attempting module imports")
    from . import util
    util.debug("Util functions imported successfully")

    from .classes.PAControl import PA_PT_ContextControlPanel
    from .configuration import PA_AddonPrefs
    from .classes.themes.PAThemePanel import PA_PT_ThemePanel, PA_PT_ThemeEditingPanel, PA_UL_ThemeList, PA_PT_ThemeEditing_PlayerPanel, PA_PG_ThemeEditorValues, ThemeEditor_SelectedThemeChange, PA_PT_ThemeEditing_ObjectPanel, PA_PT_ThemeEditing_BackgroundObjectPanel, PA_PT_ThemeEditing_FXPanel
    from .classes.themes.PAThemeOperators import PA_OT_NewThemeOperator, PA_OT_RefreshThemeListOperator, PA_OT_DeleteSelectedThemeOperator, PA_OT_SaveSelectedThemeAsLSTOperator, PA_OT_SaveSelectedThemeAsVGTOperator

    from .classes.themes.PAThemeHandler import PAThemeHandler

import bpy

class PA_PG_ThemeProperties(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Theme name",
        default="Unnamed theme"
    )
    iconValue: bpy.props.IntProperty(
        name="Icon value",
        default={k : i for i, k in enumerate(bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys())}["CUBE"]
    )
    loadedThemesIndex: bpy.props.IntProperty(
        name="Position in the loaded themes list"
    )

classes = [
    PA_PT_ContextControlPanel,
    PA_AddonPrefs,
    PA_PT_ThemePanel,
    PA_PT_ThemeEditingPanel,
    PA_OT_NewThemeOperator,
    PA_OT_RefreshThemeListOperator,
    PA_UL_ThemeList,
    PA_PG_ThemeProperties,
    PA_OT_DeleteSelectedThemeOperator,
    PA_PT_ThemeEditing_PlayerPanel,
    PA_PG_ThemeEditorValues,
    PA_PT_ThemeEditing_ObjectPanel,
    PA_PT_ThemeEditing_BackgroundObjectPanel,
    PA_PT_ThemeEditing_FXPanel,
    PA_OT_SaveSelectedThemeAsLSTOperator,
    PA_OT_SaveSelectedThemeAsVGTOperator
]

from . import globals

def register():
    globals.init()

    globals.customIcons = bpy.utils.previews.new()
    globals.themeIcons = bpy.utils.previews.new()

    iconsDir = os.path.join(os.path.dirname(__file__), "icons")

    globals.customIcons.load("pa_logo", os.path.join(iconsDir, "pa_logo.png"), "IMAGE")

    util.debug("Registered icons")


    for cls in classes:
        bpy.utils.register_class(cls)

    util.info("Registered successfully")

    globals.themeHandler = PAThemeHandler()
    bpy.types.Scene.themeHandler = globals.themeHandler

    bpy.types.Scene.themes = bpy.props.CollectionProperty(type=PA_PG_ThemeProperties)
    bpy.types.Scene.themePanelSelectedTheme = bpy.props.IntProperty(
        name="Selected theme for editing",
        default=0,
        update=ThemeEditor_SelectedThemeChange
    )
    bpy.types.Scene.themeEditorValues = bpy.props.PointerProperty(type=PA_PG_ThemeEditorValues)
    bpy.types.Scene.lastThemeEditing = bpy.props.IntProperty(
        name="Index of the last theme edited in the loadedThemes list"
    )

    bpy.types.Scene.paCamera = None

    # can't load themes on startup because of blender's restrictcontext thing
    # annoying but hey that's just how it is
    # util.info("Loading themes...")
    # globals.themeHandler.loadThemes()
    

def unregister():
    global customIcons
    
    bpy.utils.previews.remove(globals.customIcons)
    bpy.utils.previews.remove(globals.themeIcons)

    util.debug("Unregistered icons")
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.themes
    del bpy.types.Scene.themeHandler
    
    util.info("Unregistered successfully")

if __name__ == "__main__":
    register()