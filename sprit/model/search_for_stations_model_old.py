import pytankerkoenig as tk
from geopy.geocoders import Nominatim
from enum import Enum
from sprit.resources.credentials import Credentials

class Distance(Enum):
    TWO_KM = 2
    FIVE_KM = 5
    TEN_KM = 10


class SpritType(Enum):
    e5 = "e5"
    e10 = "e10"
    diesel = "diesel"
    all = "all"


class BrandType(Enum):
    aral = "ARAL"
    shell = "Shell"
    total = "TotalEnergies"
    all = "all"


class OpenType(Enum):
    is_open = 'True'
    all = 'all'


class SortBy(Enum):
    distance = "dist"
    price = "price"


# This class is first iteration and was base for station_search_model.py and station_search_list_map_model.py
class SearchForStationsModel:
    """
    Model class for searching for gas stations based on certain criteria.
    """

    def get_nearby_stations(self, addr: str, dist: Distance, sprit_type: SpritType = SpritType.all,
                             brand: BrandType = BrandType.all, open: OpenType = OpenType.all, sort_by: SortBy = SortBy.distance):
        """
        Method to determine gas stations based on certain criteria.

        Args:
            addr (str): Address to search for nearby stations.
            dist (Distance): Enum value representing the distance to search within.
            sprit_type (SpritType, optional): Enum value representing the type of fuel. Defaults to SpritType.all.
            brand (BrandType, optional): Enum value representing the brand of the gas station. Defaults to BrandType.all.
            open (OpenType, optional): Enum value representing whether the gas station should be open. Defaults to OpenType.all.
            sort_by (SortBy, optional): Enum value representing the sorting criteria. Defaults to SortBy.distance.

        Returns:
            list: List of gas stations that match the search criteria.
        """

        # Check if an address was specified
        if len(addr) == 0:
            return ('Error: No address specified!')

        # Determine latitude and longitude from address
        lat, long = self._address_to_gps(addr)
        if lat == None or long == None:
            return ('Error: GPS coordinates could not be determined from address!')

        response_data = tk.getNearbyStations(Credentials.tankerkoenig_key, float(lat), float(long), dist.value, sprit_type.value, sort_by.value)

        result = []

        # Open and closed gas stations of all brands
        if brand.value == BrandType.all.value and open.value == OpenType.all.value:
            result = response_data['stations']

        # Only open gas stations of all brands
        elif brand.value == BrandType.all.value and open.value == OpenType.is_open.value:
            for i in range(len(response_data['stations'])):
                if (response_data['stations'][i]['isOpen']):
                    result.append(response_data['stations'][i])

        # Open and closed gas stations of a certain brand
        elif brand != BrandType.all  and open.value == OpenType.all.value:
            for i in range(len(response_data['stations'])):
                if (response_data['stations'][i]['brand'] == brand.value):
                    result.append(response_data['stations'][i])

        # Only open gas stations of a certain brand
        elif brand != BrandType.all and open.value == OpenType.is_open.value:
            for i in range(len(response_data['stations'])):
                if ((response_data['stations'][i]['brand']) == brand.value) and ((response_data['stations'][i]['isOpen'])):
                    result.append(response_data['stations'][i])
        return result

    def _address_to_gps(self, address: str):
        """
        Converts an address to GPS coordinates.

        Args:
            address (str): The address to convert.

        Returns:
            tuple: The latitude and longitude of the address, or (None, None) if the conversion failed.
        """
        try:
            geolocator = Nominatim(user_agent=Credentials.usr_agent)
            location = geolocator.geocode(address)
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except:
            return None, None