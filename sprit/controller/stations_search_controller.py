import asyncio
from sprit.view.stations_search_view import StationsSearchView
from sprit.model.stations_search_model import StationsSearchModel


class StationsSearchController:

    def __init__(self, rootView, search_callback):
        self.view = StationsSearchView(rootView, self.search_callback)
        self.model = StationsSearchModel()
        self.search_callback = search_callback

    def search_callback(self, search_query):
        self.search_callback(search_query)

