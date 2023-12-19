import tkinter as tk
from tkinter import ttk
from sprit.model.station_info_card_model import StationInfoCardModel
from sprit.view.station_info_card_view import StationInfoCard

class StationsListView:
    def __init__(self, root, stations):
        self.root = root
        self.stations = stations

        self.create_list_view()
        self.selected_card = None

    def create_list_view(self):
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.populate_listbox()

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y", padx=16)

    def populate_listbox(self):
        for station in self.stations:
            infoCardModel = StationInfoCardModel(station)
            card = StationInfoCard(self.scrollable_frame, infoCardModel, self.on_card_click)
            card.pack(fill='x', expand=True, padx=16, pady=16)

    def on_card_click(self, card):
        if self.selected_card:
            self.selected_card.toggle_select()
        self.selected_card = card
        self.selected_card.toggle_select()
        clicked_station = card.get_station()
        print(clicked_station.name)# Now you can use clicked_station for whatever you need


    def update_stations(self, new_stations):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.stations = new_stations
        self.populate_listbox()

    def filter_stations_by_id(stations, id):
        return [station for station in stations if station.id == id]

    def run(self):
        self.root.mainloop()


