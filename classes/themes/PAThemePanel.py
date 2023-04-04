from bpy.types import Panel, UIList, PropertyGroup
from bpy.props import StringProperty, FloatVectorProperty
import bpy
from ... import globals
from ...util import Colour

def ThemeEditor_UpdateCurrentThemeFromValues(context) -> None:
    scn = context.scene
    selectedThemePropertyGroup = scn.themes[scn.themePanelSelectedTheme]

    selectedTheme = globals.themeHandler.loadedThemes[selectedThemePropertyGroup.loadedThemesIndex]

    selectedTheme.themeData["name"] = scn.themeEditorValues.name

    selectedTheme.themeData["players"][0] = Colour().setFromRGBArray(scn.themeEditorValues.player1Colour, maximum=1.0)
    selectedTheme.themeData["players"][1] = Colour().setFromRGBArray(scn.themeEditorValues.player2Colour, maximum=1.0)
    selectedTheme.themeData["players"][2] = Colour().setFromRGBArray(scn.themeEditorValues.player3Colour, maximum=1.0)
    selectedTheme.themeData["players"][3] = Colour().setFromRGBArray(scn.themeEditorValues.player4Colour, maximum=1.0)
    
    selectedTheme.themeData["gui"] = Colour().setFromRGBArray(scn.themeEditorValues.gui, maximum=1.0)
    selectedTheme.themeData["guiAccent"] = Colour().setFromRGBArray(scn.themeEditorValues.guiAccent, maximum=1.0)
    selectedTheme.themeData["bg"] = Colour().setFromRGBArray(scn.themeEditorValues.bg, maximum=1.0)
    
    selectedTheme.themeData["objects"][0] = Colour().setFromRGBArray(scn.themeEditorValues.object0Colour, maximum=1.0)
    selectedTheme.themeData["objects"][1] = Colour().setFromRGBArray(scn.themeEditorValues.object1Colour, maximum=1.0)
    selectedTheme.themeData["objects"][2] = Colour().setFromRGBArray(scn.themeEditorValues.object2Colour, maximum=1.0)
    selectedTheme.themeData["objects"][3] = Colour().setFromRGBArray(scn.themeEditorValues.object3Colour, maximum=1.0)
    selectedTheme.themeData["objects"][4] = Colour().setFromRGBArray(scn.themeEditorValues.object4Colour, maximum=1.0)
    selectedTheme.themeData["objects"][5] = Colour().setFromRGBArray(scn.themeEditorValues.object5Colour, maximum=1.0)
    selectedTheme.themeData["objects"][6] = Colour().setFromRGBArray(scn.themeEditorValues.object6Colour, maximum=1.0)
    selectedTheme.themeData["objects"][7] = Colour().setFromRGBArray(scn.themeEditorValues.object7Colour, maximum=1.0)
    selectedTheme.themeData["objects"][8] = Colour().setFromRGBArray(scn.themeEditorValues.object8Colour, maximum=1.0)
    
    selectedTheme.themeData["bgObjects"][0] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject0Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][1] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject1Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][2] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject2Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][3] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject3Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][4] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject4Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][5] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject5Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][6] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject6Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][7] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject7Colour, maximum=1.0)
    selectedTheme.themeData["bgObjects"][8] = Colour().setFromRGBArray(scn.themeEditorValues.bgObject8Colour, maximum=1.0)
    
    selectedTheme.themeData["fx"][0] = Colour().setFromRGBArray(scn.themeEditorValues.fx0Colour, maximum=1.0)
    selectedTheme.themeData["fx"][1] = Colour().setFromRGBArray(scn.themeEditorValues.fx1Colour, maximum=1.0)
    selectedTheme.themeData["fx"][2] = Colour().setFromRGBArray(scn.themeEditorValues.fx2Colour, maximum=1.0)
    selectedTheme.themeData["fx"][3] = Colour().setFromRGBArray(scn.themeEditorValues.fx3Colour, maximum=1.0)
    selectedTheme.themeData["fx"][4] = Colour().setFromRGBArray(scn.themeEditorValues.fx4Colour, maximum=1.0)
    selectedTheme.themeData["fx"][5] = Colour().setFromRGBArray(scn.themeEditorValues.fx5Colour, maximum=1.0)
    selectedTheme.themeData["fx"][6] = Colour().setFromRGBArray(scn.themeEditorValues.fx6Colour, maximum=1.0)
    selectedTheme.themeData["fx"][7] = Colour().setFromRGBArray(scn.themeEditorValues.fx7Colour, maximum=1.0)
    selectedTheme.themeData["fx"][8] = Colour().setFromRGBArray(scn.themeEditorValues.fx8Colour, maximum=1.0)

    # this is so painfully inefficient

def ThemeEditor_MarkCurrentThemeAsModified(self, context) -> None:
    scn = context.scene
    selectedThemePropertyGroup = scn.themes[scn.themePanelSelectedTheme]
    if scn.lastThemeEditing == selectedThemePropertyGroup.loadedThemesIndex:
        selectedThemePropertyGroup = scn.themes[scn.themePanelSelectedTheme]

        selectedTheme = globals.themeHandler.loadedThemes[selectedThemePropertyGroup.loadedThemesIndex]
        selectedTheme.savedToDisk = False
        ThemeEditor_UpdateCurrentThemeFromValues(context)

class PA_PG_ThemeEditorValues(PropertyGroup):
    name: StringProperty(
        name="Theme name",
        default="Unnamed theme",
        update=ThemeEditor_MarkCurrentThemeAsModified
    )

    gui: FloatVectorProperty(
        name="GUI",
        subtype="COLOR",
        default=[0.58, 0.847, 0.859]
    )

    guiAccent: FloatVectorProperty(
        name="GUI accent",
        subtype="COLOR",
        default=[0.259, 0.259, 0.259]
    )

    bg: FloatVectorProperty(
        name="BG",
        subtype="COLOR",
        default=[0.129, 0.129, 0.129]
    )


    player1Colour: FloatVectorProperty(
        name="Player 1",
        subtype="COLOR",
        default=[0.898, 0.451, 0.451],
        update=ThemeEditor_MarkCurrentThemeAsModified
    )

    player2Colour: FloatVectorProperty(
        name="Player 2",
        subtype="COLOR",
        default=[0.392, 0.71, 0.965],
        update=ThemeEditor_MarkCurrentThemeAsModified
    )

    player3Colour: FloatVectorProperty(
        name="Player 3",
        subtype="COLOR",
        default=[0.506, 0.78, 0.518],
        update=ThemeEditor_MarkCurrentThemeAsModified
    )

    player4Colour: FloatVectorProperty(
        name="Player 4",
        subtype="COLOR",
        default=[1, 0.718, 0.302],
        update=ThemeEditor_MarkCurrentThemeAsModified
    )

    object0Colour: FloatVectorProperty(
        name="Object 1",
        subtype="COLOR",
        default=[0.753, 0.675, 0.882]
    )

    object1Colour: FloatVectorProperty(
        name="Object 2",
        subtype="COLOR",
        default=[0.945, 0.482, 0.722]
    )

    object2Colour: FloatVectorProperty(
        name="Object 3",
        subtype="COLOR",
        default=[0.184, 0.259, 0.427]
    )

    object3Colour: FloatVectorProperty(
        name="Object 4",
        subtype="COLOR",
        default=[0.004, 0.694, 0.694]
    )

    object4Colour: FloatVectorProperty(
        name="Object 5",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    object5Colour: FloatVectorProperty(
        name="Object 6",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    object6Colour: FloatVectorProperty(
        name="Object 7",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    object7Colour: FloatVectorProperty(
        name="Object 8",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    object8Colour: FloatVectorProperty(
        name="Object 9",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    bgObject0Colour: FloatVectorProperty(
        name="BG Object 1",
        subtype="COLOR",
        default=[0.753, 0.675, 0.882]
    )

    bgObject1Colour: FloatVectorProperty(
        name="BG Object 2",
        subtype="COLOR",
        default=[0.945, 0.482, 0.722]
    )

    bgObject2Colour: FloatVectorProperty(
        name="BG Object 3",
        subtype="COLOR",
        default=[0.184, 0.259, 0.427]
    )

    bgObject3Colour: FloatVectorProperty(
        name="BG Object 4",
        subtype="COLOR",
        default=[0.004, 0.694, 0.694]
    )

    bgObject4Colour: FloatVectorProperty(
        name="BG Object 5",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    bgObject5Colour: FloatVectorProperty(
        name="BG Object 6",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    bgObject6Colour: FloatVectorProperty(
        name="BG Object 7",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    bgObject7Colour: FloatVectorProperty(
        name="BG Object 8",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    bgObject8Colour: FloatVectorProperty(
        name="BG Object 9",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    fx0Colour: FloatVectorProperty(
        name="FX 1",
        subtype="COLOR",
        default=[0.753, 0.675, 0.882]
    )

    fx1Colour: FloatVectorProperty(
        name="FX 2",
        subtype="COLOR",
        default=[0.945, 0.482, 0.722]
    )

    fx2Colour: FloatVectorProperty(
        name="FX 3",
        subtype="COLOR",
        default=[0.184, 0.259, 0.427]
    )

    fx3Colour: FloatVectorProperty(
        name="FX 4",
        subtype="COLOR",
        default=[0.004, 0.694, 0.694]
    )

    fx4Colour: FloatVectorProperty(
        name="FX 5",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    fx5Colour: FloatVectorProperty(
        name="FX 6",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    fx6Colour: FloatVectorProperty(
        name="FX 7",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    fx7Colour: FloatVectorProperty(
        name="FX 8",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    fx8Colour: FloatVectorProperty(
        name="FX 9",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

class PA_UL_ThemeList(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index=0):
        if self.layout_type in { "DEFAULT", "COMPACT" }:
            layout.label(text=item.name + ("*" if globals.themeHandler.loadedThemes[context.scene.themes[index].loadedThemesIndex].savedToDisk == False else ""), icon_value=item.iconValue)
        else:
            layout.label(text="no")

class PA_PT_ThemePanel(Panel):
    bl_label = "Themes"
    bl_idname = "PA_PT_ThemePanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Project Arrhythmia"
    bl_options = { "DEFAULT_CLOSED" }

    def draw(self, context) -> None:
        layout = self.layout

        layout.operator("pa.refresh_theme_list", icon="FILE_REFRESH")
        
        row = layout.row()

        scn = context.scene
        row.template_list("PA_UL_ThemeList", "", scn, "themes", scn, "themePanelSelectedTheme")

        col = row.column(align=True)
        col.operator("pa.new_theme", icon="ADD", text="")
        col.separator()
        row = col.row()
        row.operator("pa.delete_selected_theme", icon="TRASH", text="")
        row.enabled = scn.themePanelSelectedTheme >= 0 and scn.themePanelSelectedTheme < len(globals.themeHandler.loadedThemes)
        
        row = layout.row()
        op = row.operator("pa.save_selected_lst", icon="FILE_TICK")
        op.filepath = globals.themeHandler.themeFolder
        op = row.operator("pa.save_selected_vgt", icon="FILE_TICK")
        op.filepath = globals.themeHandler.themeFolder

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

        scn = context.scene
        selectedThemePropertyGroup = scn.themes[scn.themePanelSelectedTheme]
        if scn.themePanelSelectedTheme < 0 or scn.themePanelSelectedTheme >= len(globals.themeHandler.loadedThemes):
            layout.enabled = False
            return
    
        selectedTheme = globals.themeHandler.loadedThemes[selectedThemePropertyGroup.loadedThemesIndex]
        if scn.lastThemeEditing != selectedThemePropertyGroup.loadedThemesIndex:
            # set props to current theme values
            scn.themeEditorValues.name = selectedTheme.themeData["name"]
            print("called")
            # stop it going crazy
            scn.lastThemeEditing = selectedThemePropertyGroup.loadedThemesIndex

        layout.prop(scn.themeEditorValues, "name")
        layout.prop(scn.themeEditorValues, "gui")
        layout.prop(scn.themeEditorValues, "guiAccent")
        layout.prop(scn.themeEditorValues, "bg")

class PA_PT_ThemeEditing_PlayerPanel(Panel):
    bl_category = "Project Arrhythmia"
    bl_idname = "PA_PT_ThemeEditing_PlayerPanel"
    bl_parent_id = "PA_PT_ThemeEditingPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Players"
    bl_options = { "DEFAULT_CLOSED" }

    def draw(self, context):
        layout = self.layout
        scn = context.scene


        for i in range(4):
            layout.prop(scn.themeEditorValues, f"player{i + 1}Colour")

class PA_PT_ThemeEditing_ObjectPanel(Panel):
    bl_category = "Project Arrhythmia"
    bl_idname = "PA_PT_ThemeEditing_ObjectPanel"
    bl_parent_id = "PA_PT_ThemeEditingPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Objects"
    bl_options = { "DEFAULT_CLOSED" }

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        for i in range(9):
            layout.prop(scn.themeEditorValues, f"object{i}Colour")

class PA_PT_ThemeEditing_BackgroundObjectPanel(Panel):
    bl_category = "Project Arrhythmia"
    bl_idname = "PA_PT_ThemeEditing_BackgroundObjectPanel"
    bl_parent_id = "PA_PT_ThemeEditingPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Background Objects"
    bl_options = { "DEFAULT_CLOSED" }

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        for i in range(9):
            layout.prop(scn.themeEditorValues, f"bgObject{i}Colour")

class PA_PT_ThemeEditing_FXPanel(Panel):
    bl_category = "Project Arrhythmia"
    bl_idname = "PA_PT_ThemeEditing_FXPanel"
    bl_parent_id = "PA_PT_ThemeEditingPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "FX"
    bl_options = { "DEFAULT_CLOSED" }

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        for i in range(9):
            layout.prop(scn.themeEditorValues, f"fx{i}Colour")

def ThemeEditor_SelectedThemeChange(self, context: bpy.types.Context):
    scn = context.scene
    selectedThemePropertyGroup = scn.themes[scn.themePanelSelectedTheme]

    selectedTheme = globals.themeHandler.loadedThemes[selectedThemePropertyGroup.loadedThemesIndex]
    if scn.lastThemeEditing != selectedThemePropertyGroup.loadedThemesIndex:
        # set props to current theme values (i hate this too, dukemz don't murder me)
        scn.themeEditorValues.name = selectedTheme.themeData["name"]
        scn.themeEditorValues.player1Colour = selectedTheme.themeData["players"][0].getRGB(maximum=1.0)
        scn.themeEditorValues.player2Colour = selectedTheme.themeData["players"][1].getRGB(maximum=1.0)
        scn.themeEditorValues.player3Colour = selectedTheme.themeData["players"][2].getRGB(maximum=1.0)
        scn.themeEditorValues.player4Colour = selectedTheme.themeData["players"][3].getRGB(maximum=1.0)

        scn.themeEditorValues.gui = selectedTheme.themeData["gui"].getRGB(maximum=1.0)
        scn.themeEditorValues.guiAccent = selectedTheme.themeData["guiAccent"].getRGB(maximum=1.0)
        scn.themeEditorValues.bg = selectedTheme.themeData["bg"].getRGB(maximum=1.0)

        scn.themeEditorValues.object0Colour = selectedTheme.themeData["objects"][0].getRGB(maximum=1.0)
        scn.themeEditorValues.object1Colour = selectedTheme.themeData["objects"][1].getRGB(maximum=1.0)
        scn.themeEditorValues.object2Colour = selectedTheme.themeData["objects"][2].getRGB(maximum=1.0)
        scn.themeEditorValues.object3Colour = selectedTheme.themeData["objects"][3].getRGB(maximum=1.0)
        scn.themeEditorValues.object4Colour = selectedTheme.themeData["objects"][4].getRGB(maximum=1.0)
        scn.themeEditorValues.object5Colour = selectedTheme.themeData["objects"][5].getRGB(maximum=1.0)
        scn.themeEditorValues.object6Colour = selectedTheme.themeData["objects"][6].getRGB(maximum=1.0)
        scn.themeEditorValues.object7Colour = selectedTheme.themeData["objects"][7].getRGB(maximum=1.0)
        scn.themeEditorValues.object8Colour = selectedTheme.themeData["objects"][8].getRGB(maximum=1.0)

        scn.themeEditorValues.bgObject0Colour = selectedTheme.themeData["bgObjects"][0].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject1Colour = selectedTheme.themeData["bgObjects"][1].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject2Colour = selectedTheme.themeData["bgObjects"][2].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject3Colour = selectedTheme.themeData["bgObjects"][3].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject4Colour = selectedTheme.themeData["bgObjects"][4].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject5Colour = selectedTheme.themeData["bgObjects"][5].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject6Colour = selectedTheme.themeData["bgObjects"][6].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject7Colour = selectedTheme.themeData["bgObjects"][7].getRGB(maximum=1.0)
        scn.themeEditorValues.bgObject8Colour = selectedTheme.themeData["bgObjects"][8].getRGB(maximum=1.0)

        scn.themeEditorValues.fx0Colour = selectedTheme.themeData["fx"][0].getRGB(maximum=1.0)
        scn.themeEditorValues.fx1Colour = selectedTheme.themeData["fx"][1].getRGB(maximum=1.0)
        scn.themeEditorValues.fx2Colour = selectedTheme.themeData["fx"][2].getRGB(maximum=1.0)
        scn.themeEditorValues.fx3Colour = selectedTheme.themeData["fx"][3].getRGB(maximum=1.0)
        scn.themeEditorValues.fx4Colour = selectedTheme.themeData["fx"][4].getRGB(maximum=1.0)
        scn.themeEditorValues.fx5Colour = selectedTheme.themeData["fx"][5].getRGB(maximum=1.0)
        scn.themeEditorValues.fx6Colour = selectedTheme.themeData["fx"][6].getRGB(maximum=1.0)
        scn.themeEditorValues.fx7Colour = selectedTheme.themeData["fx"][7].getRGB(maximum=1.0)
        scn.themeEditorValues.fx8Colour = selectedTheme.themeData["fx"][8].getRGB(maximum=1.0)

        # stop it going crazy
        scn.lastThemeEditing = selectedThemePropertyGroup.loadedThemesIndex