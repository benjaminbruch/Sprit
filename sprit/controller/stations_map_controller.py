import customtkinter

from sprit.model.stations_map_model import StationsMapModel
from sprit.view.stations_map_view import StationsMapView
class StationsMapController():

    def __init__(self):
        self.stations_map_model = StationsMapModel()
        self.stations_map_view = StationsMapView()


    def get_stations_map_view(self):
        return self.stations_map_view

    def get_station_map_model(self):
        return self.stations_map_model

    def set_selected_station_on_map(self, station):
        self.stations_map_view.set_selected_station(station)