import unittest
from src.length_of_cable import min_length_of_cable, open_file


class TestMaxLength(unittest.TestCase):
    def test_no_cables(self):
        graph = open_file("islands.csv")
        result = min_length_of_cable(graph)
        expected_result = float("inf")
        self.assertEqual(result, expected_result)

    def test_min_length(self):
        graph = open_file("islands2.csv")
        result = min_length_of_cable(graph)
        expected_result = 104
        self.assertEqual(result, expected_result)
