import bpy  # type: ignore
import socket
import json
from math import pi


class LiveView(bpy.types.Operator):
    """
    Operator that permits a live view of the boat.\n
    It just needs to receive the Euler angles from a live source.
    """
    bl_idname = "wm.live_view"
    bl_label = "Start visualization"
    bl_options = {'REGISTER', 'UNDO'}

    _timer = None

    runing = False

    def execute(self, context) -> set:
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        self.runing = True
        self.bl_label = "Stop"
        return {'RUNNING_MODAL'}

    def modal(self, context, event) -> set:
        if event.type in {'ESC'}:
            print("Finished")
            self.cancel(context)

            return {'CANCELLED'}

        if event.type == 'TIMER':

            scene = context.scene
            tool = scene.live_properties

            self.socket_connection(tool.ip_address, tool.port)

        return {'PASS_THROUGH'}

    def cancel(self, context) -> None:
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

    def socket_connection(self, address: str, port: str) -> None:
        """
        This metod uses a socket connection to receive the data in JSON format
        """

        # Create a socket object
        s = socket.socket()

        # connect to the server
        s.connect((address, int(port)))

        # receive data from the server
        data = s.recv(1024)
        data = json.loads(data)

        object = bpy.context.active_object

        object.rotation_euler[0] = data[0]  # Roll
        object.rotation_euler[1] = data[1]  # Pitch
        object.rotation_euler[2] = data[2]  # Heading

        # close the socket connection
        s.close()


def register():
    bpy.utils.register_class(LiveView)


def unregister():
    bpy.utils.unregister_class(LiveView)
