from station_model import Station

class StationsListModel:

    def __init__(self, stations: [Station]):
        self.stations = stations

    def get_stations(self):
        return self.stations

    def set_stations(self, stations: [Station]):
        self.stations = stations
