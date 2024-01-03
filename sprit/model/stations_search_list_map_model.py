from sprit.model.station_model import Station

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