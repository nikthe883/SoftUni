import unittest
from test_worker import Worker

class WorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("John",1000,100)

    def test_initialization(self):
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_work_energy_zero(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as exception:
            self.worker.work()
        
        self.assertEqual("Not enough energy.", str(exception.exception))


    def test_work_salary_increase(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)

    def test_work_energy_decrease(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_get_info_method(self):
        info = self.worker.get_info()
        self.assertEqual(info, "John has saved 0 money.")

if __name__ == "__main__":
    unittest.main()