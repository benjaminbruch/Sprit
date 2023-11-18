import pytankerkoenig as tk
from geopy.geocoders import Nominatim
from enum import Enum
from sprit.resources.credentials import Credentials
from sprit.model.station_model import Station


class Distance(Enum):
    TWO_KM = 2
    FIVE_KM = 5
    TEN_KM = 10


class SortBy(Enum):
    distance = "dist"
    price = "price"


class SpritType(Enum):
    e5 = "e5"
    e10 = "e10"
    diesel = "diesel"
    all = "all"


class SearchForStationsModel:

    def get_nearby_stations(self, address: str, dist: Distance, sprit_type: SpritType = SpritType.all,
                            sort_by: SortBy = SortBy.distance) -> [Station]:
        lat, long = self._address_to_gps(address)

        response_data = tk.getNearbyStations(Credentials.tankerkoenig_key, float(lat), float(long), dist.value,
                                             sprit_type.value,
                                             sort_by.value)

        stations = []
        for station in response_data['stations']:
            stations.append(Station(**station))

        return stations

    def _address_to_gps(self, address: str):
        geolocator = Nominatim(user_agent="FH_SWF")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None
