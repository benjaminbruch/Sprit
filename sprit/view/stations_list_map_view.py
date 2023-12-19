import tkinter


class StationsListMapView:
    def __init__(self, root, list_view, map_view):
        self.root = root
        self.root.title("Tankstellensuche")
        self.root.geometry("1920x1080")

        self.stations_list_view = list_view
        self.map_view = map_view

        self.create_paned_window()

    def create_paned_window(self):
        # Create a PanedWindow
        self.paned_window = tkinter.PanedWindow(self.root)
        self.paned_window.pack(fill=tkinter.BOTH, expand=1, padx=16, pady=16)

        # Create left frame and add it to PanedWindow
        self.left_frame = tkinter.Frame(self.paned_window)
        self.stations_list_view.canvas.pack(fill=tkinter.BOTH, expand=1)  # Ensure the list view fills the frame
        self.paned_window.add(self.left_frame)

        # Create right frame and add it to PanedWindow
        self.right_frame = tkinter.Frame(self.paned_window)  # Create a new Frame widget
        self.map_view.map_widget.pack(fill=tkinter.BOTH, expand=1)  # Ensure the map widget fills the frame
        self.paned_window.add(self.right_frame)
    def run(self):
        self.root.mainloop()