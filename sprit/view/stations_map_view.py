import tkinter
import customtkinter
import tkintermapview
from sprit.model.stations_map_model import StationsMapModel

class StationsMapView(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Configure the search bar row to not expand
        self.grid_rowconfigure(1, weight=1)  # Configure the map view row to expand

        # Create the search bar
        self.search_bar = customtkinter.CTkEntry(self, placeholder_text="type address")
        self.search_bar.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)

        # Create the map view
        self.map_view = tkintermapview.TkinterMapView(self, corner_radius=0)
        self.map_view.grid(row=1, column=0, sticky="nsew")




    def add_stations(self, stations):
        for station in stations:
            self.map_widget.set_marker(station.lat, station.lng, station.name)

    def set_selected_station(self, station):
        self.map_widget.set_position(station.lat, station.lng)



