from sprit.model.station_model import Station
from PIL import Image, ImageTk
import os

class StationsSearchListMapModel:

    def __init__(self):
        self.stations: [Station] = []
        self.sprit_type = "e10"
        self.sort_by = "Preis"
        self.selected_card = None

    def sort_stations_by(self, sort_by: str):
        if sort_by == "Entfernung":
            self.stations = sorted(self.stations, key=lambda station: station.dist, reverse=False)
        else:
            self.stations = sorted(self.stations, key=lambda station: station.price, reverse=False)

    def set_sprit_type(self, sprit_type: str):
        if sprit_type == "E5":
            self.sprit_type = "e5"
        elif sprit_type == "E10":
            self.sprit_type = "e10"
        else:
            self.sprit_type = "diesel"

    def update_price_by_sprit_type(self):
        for station in self.stations:
            if self.sprit_type == "e5":
                station.price = station.e5
            elif self.sprit_type == "e10":
                station.price = station.e10
            else:
                station.price = station.diesel

    def get_gas_station_icon(self, station_name) -> ImageTk.PhotoImage:
        print(os.getcwd())
        try:
            img = Image.open("./resources/stations_icons/"+station_name+".png")
        except:
            img = Image.open("./resources/stations_icons/gas_station_icon.png")
        photo = ImageTk.PhotoImage(img)
        return photo
