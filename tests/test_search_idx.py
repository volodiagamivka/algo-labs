import sys

sys.path.append("/Users/voloda/Desktop/algo/lab7/src")
from search_idx import search_idx_rabbin_karp
import unittest


class TestSearchIdx(unittest.TestCase):
    def test_no_occurrences(self):
        haystack = "crocodile"
        needle = "dog"
        expected_result = "Не знайдено індексів входження"
        self.assertEqual(search_idx_rabbin_karp(needle, haystack), expected_result)

    def test_one_occurence(self):
        haystack = "crocodile"
        needle = "dil"
        expeected_result = 5
        self.assertEqual(search_idx_rabbin_karp(needle, haystack), expeected_result)

    def test_collision(self):
        haystack = "ababababababab"
        needle = "abab"
        expected_result = 0
        self.assertEqual(search_idx_rabbin_karp(needle, haystack), expected_result)



if __name__ == "__main__":
    unittest.main()
