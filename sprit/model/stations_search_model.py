import pytankerkoenig as pytking
from geopy.geocoders import Nominatim
from sprit.resources.credentials import Credentials
from sprit.model.station_model import Station, SortBy


class GeocodingError(Exception):
    pass


class StationsSearchModel:

    def __init__(self):
        self.stations = []

    def get_nearby_stations(self, address: str, dist: int,
                            sort_by: SortBy = SortBy.distance, sprit_type = "e10") -> [Station]:
        lat, long = self._address_to_gps(address)

        response_data = pytking.getNearbyStations(Credentials.tankerkoenig_key, float(lat), float(long), dist,
                                                  "all",
                                                  sort_by.value)

        self.stations = []
        for station in response_data['stations']:
            sprit_type_to_price = {
                'e5': station['e5'],
                'e10': station['e10'],
                'diesel': station['diesel']
            }
            station = Station(
                id=station['id'],
                name=station['name'],
                brand=station['brand'],
                street=station['street'],
                place=station['place'],
                lat=station['lat'],
                lng=station['lng'],
                dist=station['dist'],
                price=sprit_type_to_price[sprit_type],
                diesel=station['diesel'],
                e5=station['e5'],
                e10=station['e10'],
                isOpen=station['isOpen'],
                houseNumber=station['houseNumber'],
                postCode=station['postCode']
            )

            self.stations.append(station)

        return self.stations

    def _address_to_gps(self, address: str):
        geolocator = Nominatim(user_agent="FH_SWF")
        try:
            location = geolocator.geocode(address)
            if location:
                return location.latitude, location.longitude
            else:
                raise GeocodingError(f"No location found for address: {address}")
        except Exception as e:
            raise GeocodingError(e)

    def get_stations(self):
        return self.stations
