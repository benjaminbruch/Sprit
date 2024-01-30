from sprit.model.station_model import Station
from PIL import Image, ImageTk
import os
from sprit.resources import helper


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
        self.photo = None              # Reference to the currently selected station icon

    def sort_stations_by(self, sort_by: str):
        """
        Sorts the stations based on distance or price.

        Args:
            sort_by: A string indicating the sorting criterion ("Entfernung" for distance, others for price).
        """
        if sort_by == "Preis":
            self.stations = sorted(self.stations,
                                   key=lambda station: float('inf') if station.price is None else station.price,
                                   reverse=False)
        elif sort_by == "Entfernung":
            self.stations = sorted(self.stations,
                                   key=lambda station: float('inf') if station.dist is None else station.dist,
                                   reverse=False)

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

        # Get the directory of the currently running script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        try:

            img = Image.open( helper.find_data_file(f"{station_name}.png"))
        except FileNotFoundError as e:
            # If specific station icon is not found, use a default icon
            helper.find_data_file(f"gas_station_icon.png")
            img = Image.open(helper.find_data_file(f"gas_station_icon.png"))
        self.photo = ImageTk.PhotoImage(img)
        return self.photo
