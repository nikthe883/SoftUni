from unittest import TestCase, main
from railway_station import RailwayStation
from collections import deque

class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation('Plovdiv')

    def test_structure(self):
        self.assertEqual(RailwayStation.__base__.__name__, "object")
        self.assertTrue(hasattr(self.station, "arrival_trains"))
        self.assertTrue(hasattr(self.station, "departure_trains"))

        self.assertTrue(isinstance(getattr(RailwayStation, "name"), property))

        assert isinstance(self.station.arrival_trains, deque)
        assert isinstance(self.station.departure_trains, deque)


    def test_initialization(self):

        self.assertEqual(self.station.name, 'Plovdiv')
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.assertEqual(self.station.departure_trains, deque([]))



if __name__ == '__main__':
    main()

    

