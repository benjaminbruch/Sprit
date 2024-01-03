
import customtkinter
from sprit.model.stations_list_model import StationsListModel
from sprit.model.station_info_card_model import StationInfoCardModel
from sprit.view.station_info_card_view import StationInfoCardView


class StationsListView(customtkinter.CTkScrollableFrame):
    def __init__(self, master, stations_list_model: StationsListModel, **kwargs):
        super().__init__(master, **kwargs)

        self.model: StationsListModel = stations_list_model

    def update_view(self):
        for i, station in enumerate(self.model.stations):
            station_info_card = StationInfoCardView(self, StationInfoCardModel(station), fg_color='#4e5d77')
            station_info_card.grid(row=i, column=0, padx=10, pady=(10, 10), sticky="news")
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)
        
