from cat import Cat
from unittest import TestCase, main

class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Tom")
        self.cat.fed = False

    def test_successful_initial(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_size_increase(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)
        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)

    def test_cat_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_cat_cannot_eat_after_fed_exeption(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as exception:
            self.cat.eat()
        
        self.assertEqual("Already fed.", str(exception.exception))

    def test_cat_cannot_sleep_before_fed_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
      

    def test_cat_not_sleepy_after_sleep(self):
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)



if __name__ == "__main__":
    main()