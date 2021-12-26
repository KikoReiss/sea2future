import bpy  # type: ignore
from Sea2Future.panels import live_view_panel, load_file_panel  # type: ignore

bl_info = {
    "name": "Sea2Future",
    "author": "Francisco Reis",
    "version": (0, 2, 2),
    "blender": (2, 90, 0),
    "description": "Sea2Future addon",
    "location": "Collection Properties",
    "category": "Development",
}


class MainPanel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'collection'
    bl_category = "Sea2Future"
    bl_options = {"HEADER_LAYOUT_EXPAND"}
    bl_idname = "VIEW_3D_PT_main_panel"
    bl_label = "Sea2Future"

    def draw(self, context):
        pass


classes = (
    live_view_panel,
    load_file_panel
)


def register():
    """
    Is a function which only runs when enabling the add-on, this means the module can be loaded without activating the add-on
    """
    bpy.utils.register_class(MainPanel)
    for cls in classes:
        cls.register()


def unregister():
    """
    Is a function to unload anything setup by register, this is called when the add-on is disabled.
    """
    bpy.utils.unregister_class(MainPanel)
    for cls in classes:
        cls.unregister()
