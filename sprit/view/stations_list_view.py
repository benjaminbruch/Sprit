import customtkinter
from tkinter import ttk
from sprit.model.station_info_card_model import StationInfoCardModel
from sprit.view.station_info_card_view import StationInfoCard

class StationsListView(customtkinter.CTkScrollableFrame):
    def __init__(self, model):

        super().__init__()
        self.model: StationInfoCardModel = model
        self.station_info_card_views = []

    def updateView(self):

        
