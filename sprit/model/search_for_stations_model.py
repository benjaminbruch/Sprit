import pytankerkoenig as tk
from geopy.geocoders import Nominatim
from enum import Enum
from resources.credentials import Credentials
from model.station_model import Station

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

class SearchForStationsModel:

    # def get_nearby_stations(self, address: str, dist: Distance, sprit_type: SpritType = SpritType.all,
    #                         sort_by: SortBy = SortBy.distance) -> [Station]:

    def get_nearby_stations(self, addr: str, dist: Distance, sprit_type: SpritType = SpritType.all,
                             brand: BrandType = BrandType.all, open: OpenType = OpenType.all, sort_by: SortBy = SortBy.distance) -> [Station]:
        print('Adresse:', addr)
    # Längen und Breitengrad aus Adresse ermitteln
        lat, long = self._address_to_gps(addr)

        response_data = tk.getNearbyStations(Credentials.tankerkoenig_key, float(lat), float(long), dist.value, sprit_type.value, sort_by.value)

# Erste Version eine Liste der Tankstellen zu erstellen
        # stations = []
        # for station in response_data['stations']:
        #     stations.append(Station(**station))
        # return stations

        #Ergebnis Liste
        result = []

        # geöffnete und geschlossene Tankstellen aller Marken
        if brand.value == BrandType.all.value and open.value == OpenType.all.value:
            print("all Brands Open&Close")
            result = response_data
            #print("all Brands Open&Close ====> OK!")

        # Nur geöffnete Tankstellen aller Marken
        elif brand.value == BrandType.all.value and open.value == OpenType.is_open.value:
            print("all Brands only Open")
            for i in range(len(response_data['stations'])):
                if (response_data['stations'][i]['isOpen']):
                    #print('If ==> OK!')
                    result.append(response_data['stations'][i]['name'])
            print("all Brands only Open ====> OK!")

        #geöffnete und geschlossene Tankstellen einer bestimmetn Marke
        elif brand != BrandType.all  and open.value == OpenType.all.value:
            print("special Brand Open&Close")
            for i in range(len(response_data['stations'])):
                if (response_data['stations'][i]['brand'] == brand.value):
                    #print('If ===>Okay!')
                    result.append(response_data['stations'][i]['name'])
            print("special Brand Open&Close ====> OK!")

        #Nur geöffnete Tankstellen einer bestimmetn Marke
        elif brand != BrandType.all and open.value == OpenType.is_open.value:
            print("special Brand only Open")
            for i in range(len(response_data['stations'])):
                if ((response_data['stations'][i]['brand']) == brand.value) and ((response_data['stations'][i]['isOpen'])):
                    #print('IF ====> OK!')
                    result.append(response_data['stations'][i]['name'])
            print("special Brand only Open ====> OK!")
        return result

    def _address_to_gps(self, address: str):
        geolocator = Nominatim(user_agent=Credentials.usr_agent)
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None
