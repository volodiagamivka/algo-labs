import unittest
from main import num_of_pumpkins


class TestSolution(unittest.TestCase):
    def test_1(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]

        expected_result = "1 2 3 4 5 10 9 8 7 6 11 12 13 14 15 20 19 18 17 16 21 22 23 24 25"
        self.assertEqual(num_of_pumpkins(matrix), expected_result)

    def test_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]

        expected_result = "1 2 3 4 8 7 6 5"
        self.assertEqual(num_of_pumpkins(matrix), expected_result)



    def test_3(self):
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected_result = "1 2 3 4 5 6"
        self.assertEqual(num_of_pumpkins(matrix), expected_result)

