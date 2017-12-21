import unittest
from unique_chars import unique_characters

class TestUniqueCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(unique_characters(""), [])
    
    def test_one_word(self):
        self.assertEqual(unique_characters("anagram"), ["n", "g", "r", "m"])
    
    def test_string_with_spaces(self):
        self.assertEqual(unique_characters("cat and dog"), ["c", "t", "n", "o", "g"])
    
    def test_string_with_uppercase_chars(self):
        self.assertEqual(unique_characters("Marm"), ["a", "r"])

if __name__ == '__main__':
    unittest.main()