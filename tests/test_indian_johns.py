import unittest
from src.indian_johns import number_of_routes


class TestIndianJohns(unittest.TestCase):
    def test_indian_johns_1(self):
        data = "3 3\naaa\ncab\ndef\n"

        with open("ijones.in", "w") as input_data:
            input_data.write(data)
        number_of_routes()

        with open("ijones.out", "r") as output_data:
            number_of_ways = output_data.read()

        expected_result = "5"

        self.assertEqual(number_of_ways, expected_result)

    def test_indian_johns_2(self):
        data = "10 1\n abcdefaghi\n"
        with open("ijones.in", "w") as input_data:
            input_data.write(data)
        number_of_routes()

        with open("ijones.out", "r") as output_data:
            number_of_ways = output_data.read()

        expected_result = "2"

        self.assertEqual(number_of_ways, expected_result)


if __name__ == "__main__":
    unittest.main()
