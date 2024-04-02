from climbing_robot import ClimbingRobot
import unittest


class TestClimbingRobot(unittest.TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'CPU', 10, 10)

    def test_init(self):
        self.assertEqual(self.robot.category, 'Mountain')
        self.assertEqual(self.robot.part_type, 'CPU')
        self.assertEqual(self.robot.capacity, 10)
        self.assertEqual(self.robot.memory, 10)
        self.assertAlmostEqual(self.robot.installed_software,[])

    def test_category_failure(self):
        with self.assertRaises(ValueError) as ex:
            self.robot = ClimbingRobot('thins', 'CPU', 10, 10)

        self.assertEqual(str(ex.exception), f"Category should be one of {self.ALLOWED_CATEGORIES}")

    def test_succeess_installed_software(self):
        check = self.robot.install_software({'name':'python','capacity_consumption':2, 'memory_consumption': 2})
        self.assertEqual(check, "Software 'python' successfully installed on Mountain part.")
        

    def test_get_used_capacity(self):
        pass


        

if __name__ == '__main__':
    unittest.main()