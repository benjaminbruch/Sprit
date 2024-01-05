import pytankerkoenig as pytking
from geopy.geocoders import Nominatim
from sprit.resources.credentials import Credentials
from sprit.model.station_model import Station, SortBy

class GeocodingError(Exception):
    """
    Custom exception class for handling geocoding errors.
    """
    pass


class StationsSearchModel:
    """
    A class to search for nearby gas stations based on a given address.

    This class utilizes the pytankerkoenig library to interact with the Tankerkönig API and
    geopy for geocoding addresses. It provides methods to convert an address to GPS coordinates
    and retrieve nearby gas stations.
    """

    def __init__(self):
        """
        Initializes the StationsSearchModel with an empty list of stations.
        """
        self.stations = []

    def get_nearby_stations(self, address: str, dist: int,
                            sort_by: SortBy = SortBy.distance, sprit_type = "e10") -> [Station]:
        """
        Fetches nearby gas stations based on a given address.

        Args:
            address: The address to be converted to GPS coordinates.
            dist: Radius in kilometers within which to search for gas stations.
            sort_by: Enum specifying how to sort the stations (e.g., by distance).
            sprit_type: Type of fuel to consider for price (e.g., "e10", "diesel").

        Returns:
            A list of Station objects representing the nearby gas stations.

        Raises:
            GeocodingError: If geocoding of the address fails or no location is found.
        """
        lat, long = self._address_to_gps(address)

        # Fetch stations using the Tankerkönig API
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
        """
        Converts an address to GPS coordinates.

        Args:
            address: The address to be geocoded.

        Returns:
            A tuple containing the latitude and longitude of the address.

        Raises:
            GeocodingError: If geocoding of the address fails or no location is found.
        """
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
        """
        Returns the list of gas stations.

        Returns:
            A list of Station objects.
        """
        return self.stations
