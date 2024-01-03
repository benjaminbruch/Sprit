import customtkinter
from tkintermapview import TkinterMapView
from sprit.view.stations_list_view import StationsListView
from sprit.model.stations_list_model import StationsListModel
from sprit.model.stations_search_list_map_model import StationsSearchListMapModel


class StationsSearchListMapView(customtkinter.CTkFrame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.model = StationsSearchListMapModel()

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=4)
        master.grid_rowconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.frame_left.grid_rowconfigure(0, weight=0)
        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.grid_columnconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        self.price_distance_button = customtkinter.CTkSegmentedButton(self.frame_left, values=["Preis", "Distanz"])
        self.price_distance_button.set("Preis")
        self.price_distance_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 10), sticky="ew")

        self.stations_list_model = StationsListModel(self.model.stations)
        self.stations_list = StationsListView(self.frame_left, self.stations_list_model)
        self.stations_list.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.stations_list.update_view()

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

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = customtkinter.CTk()
    app.title("Sprit - Tankstellensuche")
    app.geometry("1280x1024")
    app.minsize(1280, 1024)

    # Configure the grid to expand
    app.grid_columnconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    view = StationsSearchListMapView(app)
    view.start()
