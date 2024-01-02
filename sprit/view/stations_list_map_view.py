import customtkinter
from tkintermapview import TkinterMapView


class StationsListMapView(customtkinter.CTk):
    def __init__(self, list_view, map_view):

        super().__init__()

        window_name = "Tankstellensuche"
        width = 800
        height = 600

        self.title(window_name)
        self.geometry(str(width) + "x" + str(height))
        self.minsize(width, height)

        self.list_view = list_view
        self.map_view = map_view

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = self.list_view
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = self.map_view
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

    def start(self):
        self.mainloop()
