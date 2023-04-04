from bpy.types import Operator
from bpy.utils import register_class
import bpy
from math import pi

# min + max orthographic sizes
minZoom = 1
maxZoom = 20
defaultZoom = 5

class PA_OT_SetUpSceneOperator(Operator):
    bl_idname = "pa.set_up_scene"
    bl_label = "Set up scene"
    bl_description = "Set up the current scene to be used to edit a PA level."

    def execute(self, context):
        scn = context.scene
        ops = bpy.ops

        # clear current scene
        ops.object.hide_view_clear()
        ops.object.select_all(action="SELECT")
        ops.object.delete(use_global=True)

        # set up camera
        viewLayer = context.view_layer
        
        cameraData = bpy.data.cameras.new(name="PA Camera")
        cameraData.type = "ORTHO"
        cameraData.ortho_scale = defaultZoom
        
        cameraObject = bpy.data.objects.new(name="PA Camera", object_data=cameraData)
        
        viewLayer.active_layer_collection.collection.objects.link(cameraObject)
        
        cameraObject.location = (0, -10, 0)
        cameraObject.rotation_euler.x = pi * 0.5
        
        con = cameraObject.constraints.new(type="LIMIT_LOCATION")
        con.use_max_y = True
        con.use_min_y = True
        con.max_y = -10
        con.min_y = -10
        
        return { "FINISHED" }

if __name__ == "__main__":
    register_class(PA_OT_SetUpSceneOperator)