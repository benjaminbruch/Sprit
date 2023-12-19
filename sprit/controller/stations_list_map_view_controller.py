import asyncio
from sprit.controller.stations_search_controller import StationsSearchController
from sprit.view.stations_list_map_split_view import StationsListMapSplitView

class StationsListMapViewController:
    def __init__(self, root):
        self.root = root
        self.stations_search_controller = StationsSearchController(self.root, self.search_callback)
        self.split_view = StationsListMapSplitView(self.root)



    def run(self):
        self.split_view.run()

    def search_callback(self, search_query):
        searchModel = self.stations_search_controller.model
        stations = searchModel.get_nearby_stations(search_query, 5)
        self.split_view.stations_list_view.update_stations(stations)
        self.split_view.map_view.add_stations(stations)


