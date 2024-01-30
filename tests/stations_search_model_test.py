import unittest
from sprit.model.stations_search_model import StationsSearchModel, SortBy, GeocodingError
from sprit.model.station_model import Station


class TestStationsSearchModel(unittest.TestCase):
    def setUp(self):
        self.search_model = StationsSearchModel()

    def test_get_nearby_stations(self):
        try:
            stations = self.search_model.get_nearby_stations("Berlin, Germany", 10, SortBy.distance, "e10")
            self.assertIsInstance(stations, list)
            for station in stations:
                self.assertIsInstance(station, Station)
        except GeocodingError as e:
            self.fail(f"GeocodingError was raised: {e}")

    def test_address_to_gps(self):
        try:
            lat, long = self.search_model._address_to_gps("Berlin, Germany")
            self.assertIsInstance(lat, float)
            self.assertIsInstance(long, float)
        except GeocodingError as e:
            self.fail(f"GeocodingError was raised: {e}")


if __name__ == '__main__':
    unittest.main()