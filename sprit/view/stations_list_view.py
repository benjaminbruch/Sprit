
import customtkinter
from sprit.model.station_info_card_model import StationInfoCardModel
from sprit.view.station_info_card_view import StationInfoCardView


class StationsListView(customtkinter.CTkScrollableFrame):
    def __init__(self, master, on_station_card_click, **kwargs):
        super().__init__(master, **kwargs)
        self.on_station_card_click = on_station_card_click
        self.selected_card = None

    def update_view(self, stations):
        for i, station in enumerate(stations):
            station_info_card = StationInfoCardView(self, StationInfoCardModel(station), fg_color='#4e5d77')
            station_info_card.grid(row=i, column=0, padx=10, pady=(10, 10), sticky="news")
            self.bind_click_event_to_all_children(station_info_card, station_info_card, station)
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)

    # def bind_click_event_to_all_children(self, parent, station):
    #     for child in parent.winfo_children():
    #         child.bind("<Button-1>", lambda event, s=station, card=child: self.on_station_card_click(s, card, event))
    #         self.bind_click_event_to_all_children(child, station)

    def bind_click_event_to_all_children(self, parent, card, station):
        def on_click(event):
            self.on_station_card_click(station, card, event)

        card.bind("<Button-1>", on_click)

        for child in parent.winfo_children():
            if child == card:
                continue  # Skip the card itself, we've already bound the click event

            child.bind("<Button-1>", lambda event, s=station, c=card: self.on_station_card_click(s, c, event))
            self.bind_click_event_to_all_children(child, card, station)