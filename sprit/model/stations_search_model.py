import pytankerkoenig as pytking
from geopy.geocoders import Nominatim
from sprit.resources.credentials import Credentials
from sprit.model.station_model import Station, SortBy, SpritType



class StationsSearchModel:

    def __init__(self):
        self.stations = []

    def get_nearby_stations(self, address: str, dist: int, sprit_type: SpritType = SpritType.all,
                            sort_by: SortBy = SortBy.distance) -> [Station]:
        lat, long = self._address_to_gps(address)

        response_data = pytking.getNearbyStations(Credentials.tankerkoenig_key, float(lat), float(long), dist,
                                                  sprit_type.value,
                                                  sort_by.value)

        self.stations = []
        for station in response_data['stations']:
            self.stations.append(Station(**station))

        return self.stations

    def _address_to_gps(self, address: str):
        geolocator = Nominatim(user_agent="FH_SWF")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None

    def get_stations(self):
        return self.stations