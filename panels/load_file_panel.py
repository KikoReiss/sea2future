import bpy  # type: ignore
from Sea2Future.operators import load_file_operator  # type: ignore


class LoadFilePanel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'collection'
    bl_category = "Sea2Future"
    bl_options = {"HEADER_LAYOUT_EXPAND"}
    bl_parent_id = "VIEW_3D_PT_main_panel"
    bl_idname = "VIEW_3D_PT_animation_panel"
    bl_label = "Load File"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tool = scene.animation_properties

        layout.prop(tool, "attitude_type", text="Attitude Type")
        layout.prop(tool, "file_path")

        layout.operator("wm.load_file")


class Properties(bpy.types.PropertyGroup):

    attitude_type: bpy.props.EnumProperty(
        name="Connection Types:",
        description="Choose the connection type",
        items=[
            ('OP1', "Full", "Using both position and rotation"),
            ('OP2', "Position", "Only position"),
            ('OP3', "Rotation", "Only rotation, using euler angles"),
        ]
    )

    file_path: bpy.props.StringProperty(
        name="File",
        description="Choose your file:",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )


classes = (
    Properties,
    LoadFilePanel
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    load_file_operator.register()

    bpy.types.Scene.animation_properties = bpy.props.PointerProperty(
        type=Properties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    load_file_operator.unregister()

    del bpy.types.Scene.animation_properties
