import bpy  # type: ignore
from Sea2Future.operators import live_view_operator  # type: ignore


class LiveViewPanel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'collection'
    bl_category = "Sea2Future"
    bl_options = {"HEADER_LAYOUT_EXPAND"}
    bl_parent_id = "VIEW_3D_PT_main_panel"
    bl_idname = "VIEW_3D_PT_live_panel"
    bl_label = "Live View"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tool = scene.live_properties

        layout.prop(tool, "connection_types", text="Connection Type")

        if tool.connection_types == 'OP1':
            layout.prop(tool, "ip_address")
            layout.prop(tool, "port")

        layout.operator("wm.live_view", text="Start Visualization")


class Properties(bpy.types.PropertyGroup):

    connection_types: bpy.props.EnumProperty(
        name="Connection Type",
        description="Choose the connection type",
        items=[
            ('OP0', "", ""),
            ('OP1', "Socket", "Socket communication"),
        ]
    )

    ip_address: bpy.props.StringProperty(
        name="IP address",
        description="The IP address to connect",
        default="",
        maxlen=1024,
    )

    port: bpy.props.StringProperty(
        name="Port",
        description="The port to connect",
        default="",
        maxlen=1024,
    )


classes = (
    Properties,
    LiveViewPanel
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    live_view_operator.register()

    bpy.types.Scene.live_properties = bpy.props.PointerProperty(
        type=Properties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    live_view_operator.unregister()

    del bpy.types.Scene.live_properties
