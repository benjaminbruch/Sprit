from sprit.view.stations_list_view import StationsListView
from sprit.model.stations_list_model import StationsListModel

class StationsListController:
    def __init__(self, root, selected_station_callback):
        self.stations_list_model = StationsListModel([])
        self.stations_list_view = StationsListView(root, self.stations_list_model, selected_station_callback)

    def update_stations(self, stations):
        self.stations_list_model.set_stations(stations)
        self.stations_list_view.update_stations(stations)

    def get_selected_station(self):
        return self.stations_list_model.get_selected_station()

    def get_list_view(self):
        return self.stations_list_view

