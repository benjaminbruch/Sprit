from sprit.model.station_model import Station

class StationsListModel:

    def __init__(self, stations: [Station]):
        self.stations = stations
        self.selected_station = None

    def get_stations(self):
        return self.stations

    def set_stations(self, stations: [Station]):
        self.stations = stations

    def get_selected_station(self):
        return self.selected_station

    def set_selected_station(self, station: Station):
        self.selected_station = station