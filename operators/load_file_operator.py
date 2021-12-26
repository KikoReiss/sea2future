import bpy  # type: ignore
import pandas
import numpy as np


class LoadFile(bpy.types.Operator):
    """
    Operator that has the capacity to create an animation based on a file.\n
    It can simulate the attitude based on only the position, rotation or both.
    """

    bl_idname = "wm.load_file"
    bl_label = "load File"
    bl_options = {'REGISTER', 'UNDO'}

    COLUMNS = ["center.x [m]", "center.y [m]", "center.z [m]",
               "roll [deg]", "pitch [deg]", "yaw [deg]"]

    def execute(self, context):
        scene = context.scene
        tool = scene.animation_properties

        dataframe = pandas.read_csv(
            tool.file_path, delimiter=';', usecols=self.COLUMNS)

        keyframe = 1

        for index, row in dataframe.iterrows():

            # Position
            x = dataframe['center.x [m]'][index]
            y = dataframe['center.y [m]'][index]
            z = dataframe['center.z [m]'][index]

            if tool.attitude_type in {'OP1', 'OP2'}:
                context.active_object.location = (float(x), float(y), float(z))

            bpy.context.active_object.keyframe_insert(
                data_path="location", frame=keyframe)

            # Rotation
            roll = np.radians(dataframe['roll [deg]'][index])
            pitch = np.radians(dataframe['pitch [deg]'][index])
            yaw = np.radians(dataframe['yaw [deg]'][index])

            if tool.attitude_type in {'OP1', 'OP3'}:
                context.active_object.rotation_euler = (float(roll), float(pitch), float(yaw))

            bpy.context.active_object.keyframe_insert(
                data_path="rotation_euler", frame=keyframe)

            keyframe += 1

        scene.frame_end = keyframe

        return {'FINISHED'}


def register():
    bpy.utils.register_class(LoadFile)


def unregister():
    bpy.utils.unregister_class(LoadFile)
