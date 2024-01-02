import customtkinter
from tkinter import ttk
from sprit.model.stations_list_model import StationsListModel
from sprit.view.station_info_card_view import StationInfoCard

class StationsListView(customtkinter.CTk):
    def __init__(self, model):
        super().__init__()

        self.model: StationsListModel = model
        self.station_cards = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")

    def update_view(self):
        for i, value in enumerate(self.model.stations):
            station_info_card = StationInfoCard(self, value)
            self.scrollable_frame.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.station_cards.append(station_info_card)

        
