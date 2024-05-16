import unittest

from src.number_of_islands import Islands



class NumIslands(unittest.TestCase):
    def test_zero_islands(self):
        island = Islands()

        matrix = [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        assert island.num_of_islands(matrix) == 0

    def test_two_islands(self):
        islands = Islands()

        matrix = [
            ["1", "0", "0", "0", "0"],
            ["1", "0", "1", "0", "0"],
            ["0", "0", "1", "1", "1"],
            ["0", "1", "0", "0", "0"],
        ]
        assert islands.num_of_islands(matrix) == 2

    def test_one_island(self):
        islands = Islands()

        matrix = [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
        ]

        assert islands.num_of_islands(matrix) == 1


if __name__ == "__main__":
    unittest.main()
