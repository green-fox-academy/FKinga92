import unittest
from sum import Numbers

class TestSumma(unittest.TestCase):

    def test_sum_of_empty(self):
        my_number = Numbers()
        list_of_numbers = []
        self.assertEqual(my_number.summa(list_of_numbers), 0)
    
    def test_sum_of_one_element(self):
        my_number = Numbers()
        list_of_numbers = [2]
        self.assertEqual(my_number.summa(list_of_numbers), 2)
    
    def test_sum_of_multiple_elements(self):
        my_number = Numbers()
        list_of_numbers = [3, 2, 5]
        self.assertEqual(my_number.summa(list_of_numbers), 10)
    
    def test_sum_of_null(self):
        my_number = Numbers()
        list_of_numbers = None
        self.assertEqual(my_number.summa(list_of_numbers), "Not a list")

if __name__ == '__main__':
    unittest.main()
