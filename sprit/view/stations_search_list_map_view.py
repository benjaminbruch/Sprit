import customtkinter
from tkintermapview import TkinterMapView
from CTkMessagebox import CTkMessagebox
from sprit.view.stations_list_view import StationsListView
from sprit.model.stations_search_model import StationsSearchModel, GeocodingError
from sprit.model.station_model import Station, SortBy
from sprit.model.stations_search_list_map_model import StationsSearchListMapModel

class StationsSearchListMapView(customtkinter.CTkFrame):

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
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.model = StationsSearchListMapModel()
        self.search_model = StationsSearchModel()

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)
        master.grid_rowconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.frame_left.grid_rowconfigure(0, weight=0)
        self.frame_left.grid_rowconfigure(1, weight=0)
        self.frame_left.grid_rowconfigure(2, weight=1)
        self.frame_left.grid_columnconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        self.sprit_type_button = customtkinter.CTkSegmentedButton(self.frame_left, values=["E5", "E10", "Diesel"], command=self.set_sprit_type)
        self.sprit_type_button.set("E10")
        self.sprit_type_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="ew")

        self.price_distance_button = customtkinter.CTkSegmentedButton(self.frame_left, values=["Preis", "Entfernung"], command=self.sorty_by)
        self.price_distance_button.set("Preis")
        self.price_distance_button.grid(row=1, column=0, padx=(20, 20), pady=(20, 10), sticky="ew")

        self.stations_list = StationsListView(self.frame_left, self.on_station_card_click)
        self.stations_list.grid(row=2, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.stations_list.update_view([self.example_station])

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(10, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="Adresse eingeben")
        self.entry.grid(row=0, column=0, sticky="we", padx=(10, 0), pady=(20, 20))
        self.entry.bind("<Return>", self.search_event)

        self.search_button = customtkinter.CTkButton(master=self.frame_right,
                                                     text="Suchen",
                                                     width=90,
                                                     command=self.search_event)
        self.search_button.grid(row=0, column=1, sticky="w", padx=(20, 0), pady=(20, 20))
        self.map_widget.set_address("Deutschland")

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

        try:
            self.model.stations = self.search_model.get_nearby_stations(self.entry.get(), 5, SortBy.distance, self.model.sprit_type)
            self.model.sort_stations_by(self.price_distance_button.get())
            self.stations_list.update_view(self.model.stations)
        except GeocodingError:
            self.show_error("Adresse konnte nicht gefunden werden. Bitte überprüfen Sie Ihre Eingabe und versuchen es nochmal!")

        for station in self.model.stations:
            self.map_widget.set_marker(station.lat, station.lng, text=station.brand)

    def on_station_card_click(self, station, card, event=None):
        if self.model.selected_card is not None:
            self.model.selected_card.configure(border_width=0)
        card.configure(border_width=2, border_color="white")
        self.model.selected_card = card

        self.map_widget.set_position(station.lat, station.lng)
        self.map_widget.set_zoom(16)

    def set_sprit_type(self, event=None):
        self.model.set_sprit_type(self.sprit_type_button.get())
        self.model.update_price_by_sprit_type()
        self.stations_list.update_view(self.model.stations)

    def sorty_by(self, event=None):
        self.model.sort_stations_by(self.price_distance_button.get())
        self.stations_list.update_view(self.model.stations)

    def start(self):
        self.mainloop()

    def show_error(self, msg: str):
       CTkMessagebox(title="Info", message=msg, header=True)

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.title("Sprit - Tankstellensuche")
    app.geometry("1280x1024")
    app.minsize(1024, 768)

    # Configure the grid to expand
    app.grid_columnconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    view = StationsSearchListMapView(app)
    view.start()
