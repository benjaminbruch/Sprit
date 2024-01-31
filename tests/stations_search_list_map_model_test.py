import unittest
from sprit.model.station_model import Station
from sprit.model.stations_search_list_map_model import StationsSearchListMapModel


class TestStationsSearchListMapModel(unittest.TestCase):
    def setUp(self):
        self.search_list_map_model = StationsSearchListMapModel()
        self.station = Station(
            id="1",
            name="Station 1",
            brand="Fachhochschule Südwestfalen",
            street="Semesterprojekt - Gruppe:",
            place="Programmierung",
            lat=51.3683433,
            lng=7.6847851,
            dist=10,
            price=1.0,
            diesel=1.0,
            e5=1.0,
            e10=1.0,
            isOpen=True,
            houseNumber="A3-3",
            postCode="12345"
        )
        self.search_list_map_model.stations.append(self.station)

    def test_sort_stations_by(self):
        self.search_list_map_model.sort_stations_by("Entfernung")
        self.assertEqual(self.search_list_map_model.stations[0], self.station)

        self.station.price = 2.0
        self.search_list_map_model.sort_stations_by("Preis")
        self.assertEqual(self.search_list_map_model.stations[0], self.station)

    def test_set_sprit_type(self):
        self.search_list_map_model.set_sprit_type("E5")
        self.assertEqual(self.search_list_map_model.sprit_type, "e5")

    def test_update_price_by_sprit_type(self):
        self.search_list_map_model.set_sprit_type("E5")
        self.search_list_map_model.update_price_by_sprit_type()
        self.assertEqual(self.search_list_map_model.stations[0].price, self.station.e5)


if __name__ == '__main__':
    unittest.main()
