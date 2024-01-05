import customtkinter
from sprit.model.station_info_card_model import StationInfoCardModel
from sprit.view.station_info_card_view import StationInfoCardView


class StationsListView(customtkinter.CTkScrollableFrame):
    """
    A custom scrollable frame class for displaying a list of station information cards.

    This class extends customtkinter.CTkScrollableFrame to create a scrollable view that dynamically
    populates with information cards for each station provided. It handles the layout and binding of
    click events to each card for further interaction.
    """

    def __init__(self, master, on_station_card_click, **kwargs):
        """
        Initialize the StationsListView.

        Args:
            master: The parent widget.
            on_station_card_click: Callback function to execute when a station card is clicked.
            **kwargs: Arbitrary keyword arguments for the CTkScrollableFrame.
        """
        super().__init__(master, **kwargs)
        self.cards = []
        self.on_station_card_click = on_station_card_click
        self.selected_card = None  # Tracks the currently selected station card

    def update_view(self, stations):
        """
        Update the view with a list of stations, creating a card for each station.

        Args:
            stations: A list of station objects to be displayed.
        """
        for card in self.cards:
            card.destroy()
        self.cards = []

        for i, station in enumerate(stations):

            # Create an information card view for each station
            station_info_card = StationInfoCardView(self, StationInfoCardModel(station), fg_color='#4e5d77')
            self.cards.append(station_info_card)
            station_info_card.grid(row=i, column=0, padx=10, pady=(10, 10), sticky="news")

            # Bind a click event to each card for interaction
            self.bind_click_event_to_all_children(station_info_card, station_info_card, station)

            # Configure grid layout for each card
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)

    def bind_click_event_to_all_children(self, parent, card, station):
        """
        Bind click events to a card and all of its child widgets.

        Args:
            parent: The parent widget whose children will have the event bound.
            card: The card widget associated with the station.
            station: The station data associated with the card.
        """
        def on_click(event):
            # Callback for click event
            self.on_station_card_click(station, card, event)

        # Bind click event to the card
        card.bind("<Button-1>", on_click)

        # Bind click event to all child widgets of the card
        for child in parent.winfo_children():
            if child == card:
                continue

            child.bind("<Button-1>", lambda event, s=station, c=card: self.on_station_card_click(s, c, event))
            self.bind_click_event_to_all_children(child, card, station)
