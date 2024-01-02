import tkinter
import customtkinter
import tkintermapview
from sprit.model.stations_map_model import StationsMapModel

class StationsMapView(customtkinter.CTk):
    def __init__(self, model):

        super().__init__()
        self.model: StationsMapModel = model
        #self.map_widget = tkintermapview.TkinterMapView(self, corner_radius=0)

        #self.map_widget.set_address("Berlin")

        self.entry = customtkinter.CTkEntry(master=self,
                                       placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)




    def add_stations(self, stations):
        for station in stations:
            self.map_widget.set_marker(station.lat, station.lng, station.name)

    def set_selected_station(self, station):
        self.map_widget.set_position(station.lat, station.lng)



