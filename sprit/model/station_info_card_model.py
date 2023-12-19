class StationInfoCardModel:
    def __init__(self, station):
        self.station = station
        self.price = station.e10
        self.company_name = station.brand
        self.address = station.street + " " + str(station.house_number) + ", " + str(station.post_code) + " " + station.place
        self.extra_info = "Geöffnet" if station.is_open else "Geschlossen"
        self.distance = station.dist