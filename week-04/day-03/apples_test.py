import unittest
from apples import Apples

class ApplesTest(unittest.TestCase):

    def test_is_apple(self):
        my_apple = Apples()
        self.assertEqual(my_apple.get_apple(), "apple")

if __name__ == '__main__':
    unittest.main()
