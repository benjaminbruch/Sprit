import customtkinter



class StationsListMapView(customtkinter.CTk):

    window_name = "Tankstellensuche"
    width = 800
    height = 600

    def __init__(self, list_view, map_view):

        super().__init__()
        self.list_view = list_view
        self.map_view = map_view

        self.title(self.window_name)
        self.geometry(str(StationsListMapView.width) + "x" + str(StationsListMapView.height))
        self.minsize(StationsListMapView.width, StationsListMapView.height)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = self.list_view.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = self.map_view.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")



    def start(self):
        self.mainloop()



    # def __init__(self, root, list_view, map_view):
    #     self.root = root
    #     self.root.title("Tankstellensuche")
    #     self.root.geometry("1920x1080")
    #
    #     self.stations_list_view = list_view
    #     self.map_view = map_view
    #
    #     self.create_paned_window()
    #
    # def create_paned_window(self):
    #     # Create a PanedWindow
    #     self.paned_window = tkinter.PanedWindow(self.root)
    #     self.paned_window.pack(fill=tkinter.BOTH, expand=1, padx=16, pady=16)
    #
    #     # Create left frame and add it to PanedWindow
    #     self.left_frame = tkinter.Frame(self.paned_window)
    #     self.stations_list_view.canvas.pack(fill=tkinter.BOTH, expand=1)  # Ensure the list view fills the frame
    #     self.paned_window.add(self.left_frame)
    #
    #     # Create right frame and add it to PanedWindow
    #     self.right_frame = tkinter.Frame(self.paned_window)  # Create a new Frame widget
    #     self.map_view.map_widget.pack(fill=tkinter.BOTH, expand=1)  # Ensure the map widget fills the frame
    #     self.paned_window.add(self.right_frame)
    # def run(self):
    #     self.root.mainloop()