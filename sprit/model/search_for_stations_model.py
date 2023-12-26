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

    #Methode um Tankstellen nach bestimmten Kriterien zu ermitteln
    def get_nearby_stations(self, addr: str, dist: Distance, sprit_type: SpritType = SpritType.all,
                             brand: BrandType = BrandType.all, open: OpenType = OpenType.all, sort_by: SortBy = SortBy.distance):
        
        # Überprüfen ob eine Adresse angegeben wurde
        if len(addr) == 0:
            return ('Fehler: keine Adresse angegeben!')
        
        # Längen und Breitengrad aus Adresse ermitteln 
        lat, long = self._address_to_gps(addr)
        if lat == None or long == None:
            return ('Fehler: GPS Koordinaten konnten nicht aus Adresse ermittelt werden!')
        
        response_data = tk.getNearbyStations(Credentials.tankerkoenig_key, float(lat), float(long), dist.value, sprit_type.value, sort_by.value)

        result = []

        # geöffnete und geschlossene Tankstellen aller Marken
        if brand.value == BrandType.all.value and open.value == OpenType.all.value:
            result = response_data['stations']

        # Nur geöffnete Tankstellen aller Marken
        elif brand.value == BrandType.all.value and open.value == OpenType.is_open.value:
            for i in range(len(response_data['stations'])):
                if (response_data['stations'][i]['isOpen']):
                    result.append(response_data['stations'][i])

        #geöffnete und geschlossene Tankstellen einer bestimmetn Marke
        elif brand != BrandType.all  and open.value == OpenType.all.value:
            for i in range(len(response_data['stations'])):
                if (response_data['stations'][i]['brand'] == brand.value):
                    result.append(response_data['stations'][i])

        #Nur geöffnete Tankstellen einer bestimmetn Marke
        elif brand != BrandType.all and open.value == OpenType.is_open.value:
            for i in range(len(response_data['stations'])):
                if ((response_data['stations'][i]['brand']) == brand.value) and ((response_data['stations'][i]['isOpen'])):
                    result.append(response_data['stations'][i])
        return result

    def _address_to_gps(self, address: str):      
        try:      
            geolocator = Nominatim(user_agent=Credentials.usr_agent)
            location = geolocator.geocode(address)
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except:
            return None, None