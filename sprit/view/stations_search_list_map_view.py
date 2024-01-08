import customtkinter
from tkintermapview import TkinterMapView
from CTkMessagebox import CTkMessagebox
from sprit.view.stations_list_view import StationsListView
from sprit.view.station_data_analytics_view import StationDataAnalyticsView
from sprit.model.stations_search_model import StationsSearchModel, GeocodingError
from sprit.model.station_model import Station, SortBy
from sprit.model.stations_search_list_map_model import StationsSearchListMapModel
from sprit.model.station_data_analytics_model import StationDataAnalyticsModel
from sprit.resources.credentials import Credentials

class StationsSearchListMapView(customtkinter.CTkFrame):
    """
    A class for creating a station search and map view interface using customtkinter and TkinterMapView.

    This class integrates map view and station list view for searching and displaying gas stations.
    It allows sorting stations by price or distance and provides a map visualization of station locations.
    """

    # Static example station data for demonstration purposes
    example_station = Station(
        id="1",
        name="Station 1",
        brand="Fachhochschule Südwestfalen",
        street="Semesterprojekt - Gruppe:",
        place="Programmierung",
        lat=51.3683433,
        lng=7.6847851,
        dist=10,
        price=1.0,
        diesel=1.0,
        e5=1.0,
        e10=1.0,
        isOpen=True,
        houseNumber="A3-3",
        postCode="12345"
    )

    def __init__(self, master, *args, **kwargs):
        """
        Initialize the main frame and layout of the application.

        Args:
            master: The parent widget.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(master, *args, **kwargs)

        # Main application and model setup
        self.master = master
        self.model = StationsSearchListMapModel()
        self.search_model = StationsSearchModel()
        self.station_data_analytics_model = StationDataAnalyticsModel(Credentials.db_path)

        # Configure grid layout for master
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Configure grid layout for this frame
        self.grid_rowconfigure(0, weight=1)

        # Initialize left and right frames for controls and map
        self.frame_left = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.frame_left.grid_rowconfigure(0, weight=0)
        self.frame_left.grid_rowconfigure(1, weight=0)
        self.frame_left.grid_rowconfigure(2, weight=1)
        self.frame_left.grid_columnconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # Setup control elements for fuel type and sorting
        self.sprit_type_button = customtkinter.CTkSegmentedButton(self.frame_left, values=["E5", "E10", "Diesel"],
                                                                  command=self.set_sprit_type)
        self.sprit_type_button.set("E10")
        self.sprit_type_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="ew")

        self.price_distance_button = customtkinter.CTkSegmentedButton(self.frame_left, values=["Preis", "Entfernung"],
                                                                      command=self.sorty_by)
        self.price_distance_button.set("Preis")
        self.price_distance_button.grid(row=1, column=0, padx=(20, 20), pady=(20, 10), sticky="ew")

        # Initialize and setup station list view
        self.stations_list = StationsListView(self.frame_left, self.on_station_card_click)
        self.stations_list.grid(row=2, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.stations_list.update_view([self.example_station])

        # Setup grid layout for right frame
        self.frame_right.grid_rowconfigure(0, weight=0)  # Search entry and button row
        self.frame_right.grid_rowconfigure(1, weight=2)  # Map widget row
        self.frame_right.grid_rowconfigure(2, weight=1)  # Analytics view row
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=1)
        self.frame_right.grid_columnconfigure(2, weight=1)


        # Setup search entry and button
        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="Adresse eingeben")
        self.entry.grid(row=0, column=0, sticky="we", padx=(10, 0), pady=(20, 20))
        self.entry.bind("<Return>", self.search_event)

        self.search_button = customtkinter.CTkButton(master=self.frame_right,
                                                     text="Suchen",
                                                     width=90,
                                                     command=self.search_event)
        self.search_button.grid(row=0, column=1, sticky="w", padx=(20, 0), pady=(20, 20))

        # Initialize and setup map widget
        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(10, 0), pady=(0, 0))
        self.map_widget.set_address("Deutschland")

        # Setup station data analytics frame
        self.station_data_analytics_view = StationDataAnalyticsView(self.frame_right, self.station_data_analytics_model)
        self.station_data_analytics_view.grid(row=2, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(10, 0), pady=(20, 0))
        self.station_data_analytics_view.grid_rowconfigure(0, weight=1)
        self.station_data_analytics_view.grid_columnconfigure(0, weight=1)




    def select_first_station(self):
        """
        Select the first station from the list and zoom in on the map.
        """
        if self.model.stations:
            first_station = self.model.stations[0]
            first_card = self.stations_list.cards[0]
            self.on_station_card_click(first_station, first_card)

    def search_event(self, event=None):
        """
        Handle the search event, updating the map and station list based on the user's input.

        Args:
            event: The event triggering this method, default is None.
        """
        # Update the map address based on user input
        self.map_widget.set_address(self.entry.get())

        # Fetch and display stations based on search query
        try:
            self.model.stations = self.search_model.get_nearby_stations(self.entry.get(), 5, SortBy.distance,
                                                                        self.model.sprit_type)
            self.model.sort_stations_by(self.price_distance_button.get())
            self.stations_list.update_view(self.model.stations)
        except GeocodingError:
            self.show_error(
                "Adresse konnte nicht gefunden werden. Bitte überprüfen Sie Ihre Eingabe und versuchen es nochmal!")

        # Update map markers for each station
        for station in self.model.stations:
            self.map_widget.set_marker(station.lat, station.lng, text=station.brand + " (" + str(station.price) + " €)",
                                       icon=self.model.get_gas_station_icon(station.brand), text_color="black")

            # Select the first station after loading and displaying the stations
            self.select_first_station()

    def on_station_card_click(self, station, card, event=None):
        """
        Handle clicks on station cards, highlighting the selected station and updating the map view.

        Args:
            station: The station associated with the clicked card.
            card: The card widget that was clicked.
            event: The event triggering this method, default is None.
        """
        # Unhighlight previous selection, if any
        if self.model.selected_card is not None and self.model.selected_card.winfo_exists():
            self.model.selected_card.configure(border_width=0)


        # Highlight the selected card and update the model
        card.configure(border_width=2, border_color="white")
        self.model.selected_card = card

        # Update map position and zoom to the selected station
        self.map_widget.set_position(station.lat, station.lng)
        self.map_widget.set_zoom(18)

    def set_sprit_type(self, event=None):
        """
        Update the model and view based on the selected fuel type.

        Args:
            event: The event triggering this method, default is None.
        """
        self.model.set_sprit_type(self.sprit_type_button.get())
        self.model.update_price_by_sprit_type()
        self.stations_list.update_view(self.model.stations)

    def sorty_by(self, event=None):
        """
        Sort the station list based on the selected sorting criterion.

        Args:
            event: The event triggering this method, default is None.
        """
        self.model.sort_stations_by(self.price_distance_button.get())
        self.stations_list.update_view(self.model.stations)

    def start(self):
        """
        Start the main loop of the application.
        """
        self.mainloop()

    def show_error(self, msg: str):
        """
        Display an error message using a custom tkinter messagebox.

        Args:
            msg: The message string to be displayed.
        """
        CTkMessagebox(title="Info", message=msg, header=True)
