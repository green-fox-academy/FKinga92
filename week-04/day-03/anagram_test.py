import unittest
from anagram import is_anagram

class TestAnagram(unittest.TestCase):

    def test_two_strings(self):
        self.assertEqual(is_anagram("god", "dog"), True)
  
    def test_string_with_empty_string(self):
        self.assertEqual(is_anagram("good", ""), False)

if __name__ == '__main__':
    unittest.main()
