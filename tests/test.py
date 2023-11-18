import unittest
from sprit.model.search_for_stations_model import Distance, SearchForStationsModel


class TestSearchForStationsModel(unittest.TestCase):
    def setUp(self):
        self.model = SearchForStationsModel()

    def test_get_nearby_stations(self):
        result = self.model.get_nearby_stations('Hagen', Distance.TWO_KM)
        self.assertEqual(result[0].id, 'b5516eca-d7f4-4bd0-bc18-cd77080c7700')


if __name__ == '__main__':
    unittest.main()
