import tkinter
from sprit.view.stations_map_view import StationsMapView
from sprit.view.stations_list_view import StationsListView
from sprit.controller.stations_search_controller import StationsSearchController


class StationsListMapSplitView:
    def __init__(self, root):
        self.root = root
        self.root.title("Tankstellensuche")
        self.root.geometry("1920x1080")

        self.create_paned_window()

    def create_paned_window(self):
        # Create a PanedWindow
        self.paned_window = tkinter.PanedWindow(self.root)
        self.paned_window.pack(fill=tkinter.BOTH, expand=1, padx=16, pady=16)

        # Create left frame and add it to PanedWindow
        self.left_frame = tkinter.Frame(self.root, width=500)  # Create a new Frame widget with a width of 500 pixels
        self.left_frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width
        self.stations_list_view = StationsListView(self.left_frame, [])  # Create an instance of StationsListView
        self.stations_list_view.canvas.pack(fill=tkinter.BOTH, expand=1)  # Ensure the list view fills the frame
        self.paned_window.add(self.left_frame)

        # Create right frame and add it to PanedWindow
        self.right_frame = tkinter.Frame(self.root)  # Create a new Frame widget
        self.map_view = StationsMapView(self.right_frame)  # Create an instance of StationsMapView
        self.map_view.map_widget.pack(fill=tkinter.BOTH, expand=1)  # Ensure the map widget fills the frame
        self.paned_window.add(self.right_frame)

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    root = tkinter.Tk()

    StationsListMapSplitView(root).run()

