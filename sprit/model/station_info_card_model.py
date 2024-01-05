class StationInfoCardModel:
    """
    A model class for preparing data to be displayed on a station information card.

    This class takes a Station object and extracts relevant information for display purposes,
    such as price, company name, address, and additional details like opening status and distance.
    """

    def __init__(self, station):
        """
        Initializes the StationInfoCardModel with data from a Station object.

        Args:
            station: A Station object containing information about a specific gas station.
        """
        self.station = station  # The original Station object
        self.price = station.price  # The fuel price at the station
        self.company_name = station.brand  # The brand or company name of the station
        self.street = f"{station.street} {station.house_number}"  # The street address of the station
        self.city = station.place  # The city or locality where the station is located
        self.address = f"{self.street}\n{station.place}"  # Full address combining street and city
        self.extra_info = "Geöffnet" if station.is_open else "Geschlossen"  # Open/closed status
        self.distance = station.dist  # The distance to the station
