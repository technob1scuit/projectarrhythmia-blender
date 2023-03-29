from bpy import types, props
from . import globals

class PA_AddonPrefs(types.AddonPreferences):
    bl_idname = __package__
    levelFolderPath: props.StringProperty(
        name="Level folder path",
        subtype="FILE_PATH",
        default="%programfiles(x86)%\\Steam\\steamapps\\common\\Project Arrhythmia\\beatmaps\\editor\\"
    )

    prefabFolderPath: props.StringProperty(
        name="Prefab folder path",
        subtype="FILE_PATH",
        default="%programfiles(x86)%\\Steam\\steamapps\\common\\Project Arrhythmia\\beatmaps\\prefabs\\"
    )

    themeFolderPath: props.StringProperty(
        name="Theme folder path",
        subtype="FILE_PATH",
        default="%programfiles(x86)%\\Steam\\steamapps\\common\\Project Arrhythmia\\beatmaps\\themes\\"
    )

    # player colours

    defaultPlayerOneColour: props.FloatVectorProperty(
        name="Player 1",
        subtype="COLOR",
        default=[0.898, 0.451, 0.451]
    )

    defaultPlayerTwoColour: props.FloatVectorProperty(
        name="Player 2",
        subtype="COLOR",
        default=[0.392, 0.71, 0.965]
    )

    defaultPlayerThreeColour: props.FloatVectorProperty(
        name="Player 3",
        subtype="COLOR",
        default=[0.506, 0.78, 0.518]
    )

    defaultPlayerFourColour: props.FloatVectorProperty(
        name="Player 4",
        subtype="COLOR",
        default=[1, 0.718, 0.302]
    )

    defaultGUIColour: props.FloatVectorProperty(
        name="GUI",
        subtype="COLOR",
        default=[0.58, 0.847, 0.859]
    )

    defaultBGColour: props.FloatVectorProperty(
        name="BG",
        subtype="COLOR",
        default=[0.129, 0.129, 0.129]
    )

    # object colours

    defaultObject0Colour: props.FloatVectorProperty(
        name="Object 1",
        subtype="COLOR",
        default=[0.753, 0.675, 0.882]
    )

    defaultObject1Colour: props.FloatVectorProperty(
        name="Object 2",
        subtype="COLOR",
        default=[0.945, 0.482, 0.722]
    )

    defaultObject2Colour: props.FloatVectorProperty(
        name="Object 3",
        subtype="COLOR",
        default=[0.184, 0.259, 0.427]
    )

    defaultObject3Colour: props.FloatVectorProperty(
        name="Object 4",
        subtype="COLOR",
        default=[0.004, 0.694, 0.694]
    )

    defaultObject4Colour: props.FloatVectorProperty(
        name="Object 5",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultObject5Colour: props.FloatVectorProperty(
        name="Object 6",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultObject6Colour: props.FloatVectorProperty(
        name="Object 7",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultObject7Colour: props.FloatVectorProperty(
        name="Object 8",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultObject8Colour: props.FloatVectorProperty(
        name="Object 9",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Game compatibility settings", icon_value=globals.custom_icons["pa_logo"].icon_id)
        # file paths
        box = layout.box()
        box.label(text="Default file paths used for loading/saving", icon="FILE_FOLDER")
        box.prop(self, "levelFolderPath")
        box.prop(self, "prefabFolderPath")
        box.prop(self, "themeFolderPath")

        # default theme settings
        box = layout.box()
        box.label(text="Default theme settings", icon="EYEDROPPER")
        row = box.row()
        row.prop(self, "defaultGUIColour")
        row.prop(self, "defaultBGColour")
        playerBox = box.box()
        playerBox.label(text="Default player colours", icon="OUTLINER_OB_ARMATURE")
        row = playerBox.row()
        split = row.split(factor=0.5)
        col = split.column()
        row = col.row()
        row.prop(self, "defaultPlayerOneColour")
        row = col.row()
        row.prop(self, "defaultPlayerTwoColour")
        col = split.column()
        row = col.row()
        row.prop(self, "defaultPlayerThreeColour")
        row = col.row()
        row.prop(self, "defaultPlayerFourColour")

        objectBox = box.box()
        objectBox.label(text="Default object colours", icon="MESH_PLANE")
        
        row = objectBox.row()
        split = row.split(factor=0.5)
        col = split.column()
        row = col.row()
        row.prop(self, "defaultObject0Colour")
        row = col.row()
        row.prop(self, "defaultObject1Colour")
        row = col.row()
        row.prop(self, "defaultObject2Colour")
        row = col.row()
        row.prop(self, "defaultObject3Colour")
        row = col.row()
        row.prop(self, "defaultObject4Colour")
        
        col = split.column()

        row = col.row()
        row.prop(self, "defaultObject5Colour")
        row = col.row()
        row.prop(self, "defaultObject6Colour")
        row = col.row()
        row.prop(self, "defaultObject7Colour")
        row = col.row()
        row.prop(self, "defaultObject8Colour")