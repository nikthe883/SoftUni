from extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.test_list = IntegerList(1,2,3,"%",True)
        

    def test_init(self):
        self.assertEqual(self.test_list._IntegerList__data,[1,2,3])
    
    def test_init_with_not_int(self):
        self.assertEqual(self.test_list.get_data(),[1,2,3])

    def test_failed_add(self):
        with self.assertRaises(ValueError) as ex:
            self.test_list.add("What")


        self.assertEqual(str(ex.exception),"Element is not Integer")

    def test_success_add(self):
        self.test_list.add(4)
        self.assertEqual(self.test_list.get_data(),[1,2,3,4])

    def test_success_remove_index(self):
        self.test_list.remove_index(1)
        self.assertEqual(self.test_list.get_data(),[1,3])
    
    def test_failed_remove_index(self):
        with self.assertRaises(IndexError) as ex:
            self.test_list.remove_index(10)

        self.assertEqual(str(ex.exception),"Index is out of range")

    def test_success_get_index(self):
        self.assertEqual(self.test_list.get(1),2)

    def test_failed_get_index(self):
        with self.assertRaises(IndexError) as ex:
            self.test_list.get(10)

        self.assertEqual(str(ex.exception),"Index is out of range")

    def test_success_insert(self):
        self.test_list.insert(1,5)
        self.assertEqual(self.test_list.get_data(),[1,5,2,3])

    def test_failed_insert_index(self):
        with self.assertRaises(IndexError) as ex:
            self.test_list.insert(10,5)

        self.assertEqual(str(ex.exception),"Index is out of range")

    def test_failed_insert_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.test_list.insert(1,"the")

        self.assertEqual(str(ex.exception),"Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.test_list.get_biggest(),3)

    def test_get_index(self):
        self.assertEqual(self.test_list.get_index(2),1)


if __name__ == "__main__":
    unittest.main()