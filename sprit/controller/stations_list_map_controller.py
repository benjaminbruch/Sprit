import asyncio
from sprit.controller.stations_search_controller import StationsSearchController
from sprit.controller.stations_list_controller import StationsListController
from sprit.controller.stations_map_controller import StationsMapController
from sprit.view.stations_list_map_view import StationsListMapView

class StationsListMapController:
    def __init__(self, root):
        self.root = root

        self.stations_search_controller = StationsSearchController(self.root, self.search_input_callback)
        self.stations_list_controller = StationsListController(self.root, self.selected_station_on_list_callback)
        self.stations_map_controller = StationsMapController(self.root)

        self.stations_list_map_view = StationsListMapView(self.stations_list_controller.get_list_view(), self.stations_map_controller.get_stations_map_view())

    def run(self):
        self.stations_list_map_view.start()

    def search_input_callback(self, search_query):
        searchModel = self.stations_search_controller.model
        stations = searchModel.get_nearby_stations(search_query, 5)
        self.stations_list_controller.update_stations(stations)
        self.stations_list_map_view.map_view.add_stations(stations)

    def selected_station_on_list_callback(self, station):
        self.stations_map_controller.set_selected_station_on_map(station)

