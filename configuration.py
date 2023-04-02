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




    ########## player colours #############

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

    defaultGUIAccentColour: props.FloatVectorProperty(
        name="GUI accent",
        subtype="COLOR",
        default=[0.259, 0.259, 0.259]
    )

    defaultBGColour: props.FloatVectorProperty(
        name="BG",
        subtype="COLOR",
        default=[0.129, 0.129, 0.129]
    )




    ############ object colours #############

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


    


    ############ bg object colours #############

    defaultParallax0Colour: props.FloatVectorProperty(
        name="Parallax 1",
        subtype="COLOR",
        default=[0.753, 0.675, 0.882]
    )

    defaultParallax1Colour: props.FloatVectorProperty(
        name="Parallax 2",
        subtype="COLOR",
        default=[0.945, 0.482, 0.722]
    )

    defaultParallax2Colour: props.FloatVectorProperty(
        name="Parallax 3",
        subtype="COLOR",
        default=[0.184, 0.259, 0.427]
    )

    defaultParallax3Colour: props.FloatVectorProperty(
        name="Parallax 4",
        subtype="COLOR",
        default=[0.004, 0.694, 0.694]
    )

    defaultParallax4Colour: props.FloatVectorProperty(
        name="Parallax 5",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultParallax5Colour: props.FloatVectorProperty(
        name="Parallax 6",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultParallax6Colour: props.FloatVectorProperty(
        name="Parallax 7",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultParallax7Colour: props.FloatVectorProperty(
        name="Parallax 8",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultParallax8Colour: props.FloatVectorProperty(
        name="Parallax 9",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )


    ############ effect colours #############

    defaultEffect0Colour: props.FloatVectorProperty(
        name="Effect 1",
        subtype="COLOR",
        default=[0.753, 0.675, 0.882]
    )

    defaultEffect1Colour: props.FloatVectorProperty(
        name="Effect 2",
        subtype="COLOR",
        default=[0.945, 0.482, 0.722]
    )

    defaultEffect2Colour: props.FloatVectorProperty(
        name="Effect 3",
        subtype="COLOR",
        default=[0.184, 0.259, 0.427]
    )

    defaultEffect3Colour: props.FloatVectorProperty(
        name="Effect 4",
        subtype="COLOR",
        default=[0.004, 0.694, 0.694]
    )

    defaultEffect4Colour: props.FloatVectorProperty(
        name="Effect 5",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultEffect5Colour: props.FloatVectorProperty(
        name="Effect 6",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultEffect6Colour: props.FloatVectorProperty(
        name="Effect 7",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultEffect7Colour: props.FloatVectorProperty(
        name="Effect 8",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    defaultEffect8Colour: props.FloatVectorProperty(
        name="Effect 9",
        subtype="COLOR",
        default=[0.937, 0.922, 0.937]
    )

    def draw(self, context) -> None:

        layout = self.layout
        layout.label(text="Game compatibility settings", icon_value=globals.customIcons["pa_logo"].icon_id)
        # file paths
        box = layout.box()
        box.label(text="Default file paths used for loading/saving", icon="FILE_FOLDER")
        box.prop(self, "levelFolderPath")
        box.prop(self, "prefabFolderPath")
        box.prop(self, "themeFolderPath")

        # default theme settings
        box = layout.box()
        box.label(text="Default theme settings", icon="RESTRICT_COLOR_ON")
        row = box.row()
        split = row.split(factor=0.5)
        col = split.column()
        row = col.row()
        row.prop(self, "defaultGUIColour")
        row = col.row()
        row.prop(self, "defaultGUIAccentColour", text="GUI accent (vgt themes only)")
        col = split.column()
        row = col.row()
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


        parallaxBox = box.box()
        parallaxBox.label(text="Default parallax/background object colours", icon="MOD_OPACITY")
        
        row = parallaxBox.row()
        split = row.split(factor=0.5)
        col = split.column()
        row = col.row()
        row.prop(self, "defaultParallax0Colour")
        row = col.row()
        row.prop(self, "defaultParallax1Colour")
        row = col.row()
        row.prop(self, "defaultParallax2Colour")
        row = col.row()
        row.prop(self, "defaultParallax3Colour")
        row = col.row()
        row.prop(self, "defaultParallax4Colour")
        
        col = split.column()

        row = col.row()
        row.prop(self, "defaultParallax5Colour")
        row = col.row()
        row.prop(self, "defaultParallax6Colour")
        row = col.row()
        row.prop(self, "defaultParallax7Colour")
        row = col.row()
        row.prop(self, "defaultParallax8Colour")



        
        effectBox = box.box()
        effectBox.label(text="Default effect colours (vgt themes only)", icon="SHADERFX")
        
        row = effectBox.row()
        split = row.split(factor=0.5)
        col = split.column()
        row = col.row()
        row.prop(self, "defaultEffect0Colour")
        row = col.row()
        row.prop(self, "defaultEffect1Colour")
        row = col.row()
        row.prop(self, "defaultEffect2Colour")
        row = col.row()
        row.prop(self, "defaultEffect3Colour")
        row = col.row()
        row.prop(self, "defaultEffect4Colour")
        
        col = split.column()

        row = col.row()
        row.prop(self, "defaultEffect5Colour")
        row = col.row()
        row.prop(self, "defaultEffect6Colour")
        row = col.row()
        row.prop(self, "defaultEffect7Colour")
        row = col.row()
        row.prop(self, "defaultEffect8Colour")