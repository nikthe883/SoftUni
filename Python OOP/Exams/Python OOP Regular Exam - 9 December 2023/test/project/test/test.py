from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque

class TestRailwayStation(TestCase):

    def setUp(self) :
        self.station = RailwayStation('Plovdiv')

    def test_structure(self):
        self.assertEqual(RailwayStation.__base__.__name__, "object")
        self.assertTrue(hasattr(self.station, "arrival_trains"))
        self.assertTrue(hasattr(self.station, "departure_trains"))

    def test_instance(self):
        self.assertTrue(isinstance(getattr(RailwayStation, "name"), property))

        assert isinstance(self.station.arrival_trains, deque)
        assert isinstance(self.station.departure_trains, deque)


    def test_initialization(self):

        self.assertEqual(self.station.name, 'Plovdiv')
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.assertEqual(self.station.departure_trains, deque([]))

    def test_name_valid(self):
        self.station.name = 'Plovdiv'
        self.assertEqual(self.station.name, 'Plovdiv')

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.station.name = ""
        self.assertEqual(str(context.exception), f"Name should be more than 3 symbols!")

    def test_name_three(self):
        with self.assertRaises(ValueError) as context:
            self.station.name = "Pet"
        self.assertEqual(str(context.exception), f"Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("N140")
        self.assertEqual(self.station.arrival_trains, deque(["N140"]))

    def test_train_has_arrived_no_trains(self):
        station = RailwayStation("Test Station")
        station.new_arrival_on_board("Train A")
        # Test arrival of a train when no other trains are present
        self.assertEqual(station.train_has_arrived("Train A"), "Train A is on the platform and will leave in 5 minutes.")

    def test_train_has_arrived(self):
        station = RailwayStation("Test Station")
        
        station.new_arrival_on_board("Train A")
        station.new_arrival_on_board("Train B")
        # Test arrival of a train when no other trains are present
        self.assertEqual(station.train_has_arrived("Train A"), "Train A is on the platform and will leave in 5 minutes.")


    def test_station_has_arived_other_train(self):
        station = RailwayStation("Test Station")

        station.new_arrival_on_board("Train B")
        station.new_arrival_on_board("Train C")

        self.assertEqual(station.train_has_arrived("Train C"), "There are other trains to arrive before Train C.")

    def test_train_has_left_empty_station__expect_false(self):
        self.station.new_arrival_on_board("")
        self.station.train_has_arrived("")

        actual = self.station.train_has_left("Test Train")

        self.assertFalse(actual)


    def test_train_has_left_true(self):
        station = RailwayStation("Test Station")

        station.new_arrival_on_board("Train B")
        station.train_has_arrived("Train B")


        self.assertTrue(station.train_has_left("Train B"))

    def test_train_has_left_false(self):
        station = RailwayStation("Test Station")

        station.new_arrival_on_board("Train B")
        station.new_arrival_on_board("Train C")
        station.train_has_arrived_on_board("Train B")
        station.train_has_arrived("Train C")
       

        self.assertFalse(station.train_has_left("Train B"))






if __name__ == '__main__':
    main()

    

