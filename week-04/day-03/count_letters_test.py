import unittest
from count_letters import count_letters

class TestCountLetters(unittest.TestCase):

    def test_count_empty_string(self):
        self.assertEqual(count_letters(""), {})
    
    def test_count_letters_single_string(self):
        self.assertEqual(count_letters("alma"), {'a': 2, 'l': 1, 'm': 1})

    def test_count_string_with_spaces(self):
        self.assertEqual(count_letters("cats and cats"), {'c': 2, 'a': 3, 't': 2, "s": 2, "n": 1, "d": 1})

if __name__ == '__main__':
    unittest.main()
