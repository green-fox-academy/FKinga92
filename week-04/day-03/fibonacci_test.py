import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)
    
    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_number(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_negative_number(self):
        self.assertEqual(fibonacci(-5), "Index cannot be a negative number.")
    
    def test_fibonacci_string(self):
        self.assertEqual(fibonacci("thisisastring"), "You can only enter a number.")


if __name__ == '__main__':
    unittest.main()
