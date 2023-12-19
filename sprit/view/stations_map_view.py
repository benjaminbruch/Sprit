import tkinter
import tkintermapview

class StationsMapView:
    def __init__(self, root):
        self.map_widget = None
        self.root = root
        self.create_map_widget()

    def create_map_widget(self):
        self.map_widget = tkintermapview.TkinterMapView(self.root, width=800, height=600, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def run(self):
        self.root.mainloop()

    def add_stations(self, stations):
        for station in stations:
            self.map_widget.set_marker(station.lat, station.lng, station.name)

    def set_selected_station(self, station):
        self.map_widget.set_position(station.lat, station.lng)



