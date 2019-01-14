from tkinter import Tk


class ApkGenerator(Tk):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.title("ApkGenerator")
        self._center_self()
        self._deploy_components()

    def _center_self(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        client_width = int(screen_width * 0.7)
        client_heith = int(screen_height*0.8)
        client_x_position = int((screen_width - client_width)/2)
        client_y_position = int((screen_height - client_heith)/2)
        self.geometry('{}x{}'.format(client_width, client_heith))
        self.geometry('+{}+{}'.format(client_x_position, client_y_position))

    def _deploy_components(self):
        pass
