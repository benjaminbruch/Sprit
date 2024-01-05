from sprit.model.station_model import Station
from PIL import Image, ImageTk


class StationsSearchListMapModel:
    """
    A class for managing a list of gas stations, their sorting, and fuel type preferences in a map view.

    This class handles the logic for sorting stations based on distance or price, setting the preferred fuel type,
    updating station prices based on the selected fuel type, and loading station icons for the map view.
    """

    def __init__(self):
        """
        Initializes the StationsSearchListMapModel with default values.
        """
        self.stations: [Station] = []  # List of Station objects
        self.sprit_type = "e10"        # Default fuel type
        self.sort_by = "Preis"         # Default sorting preference
        self.selected_card = None      # Reference to the currently selected station card

    def sort_stations_by(self, sort_by: str):
        """
        Sorts the stations based on distance or price.

        Args:
            sort_by: A string indicating the sorting criterion ("Entfernung" for distance, others for price).
        """
        if sort_by == "Entfernung":
            self.stations = sorted(self.stations, key=lambda station: station.dist, reverse=False)
        else:
            self.stations = sorted(self.stations, key=lambda station: station.price, reverse=False)

    def set_sprit_type(self, sprit_type: str):
        """
        Sets the preferred fuel type for price display.

        Args:
            sprit_type: A string indicating the fuel type ("E5", "E10", or "diesel").
        """
        if sprit_type == "E5":
            self.sprit_type = "e5"
        elif sprit_type == "E10":
            self.sprit_type = "e10"
        else:
            self.sprit_type = "diesel"

    def update_price_by_sprit_type(self):
        """
        Updates the price of each station based on the selected fuel type.
        """
        for station in self.stations:
            if self.sprit_type == "e5":
                station.price = station.e5
            elif self.sprit_type == "e10":
                station.price = station.e10
            else:
                station.price = station.diesel

    def get_gas_station_icon(self, station_name) -> ImageTk.PhotoImage:
        """
        Retrieves the icon image for a given gas station.

        Args:
            station_name: The name of the gas station.

        Returns:
            An ImageTk.PhotoImage object representing the station's icon.
        """
        try:
            img = Image.open(f"sprit/resources/stations_icons/{station_name}.png")
        except FileNotFoundError:
            # If specific station icon is not found, use a default icon
            img = Image.open("sprit/resources/stations_icons/gas_station_icon.png")
        photo = ImageTk.PhotoImage(img)
        return photo
