import sys

sys.path.append("/Users/voloda/Desktop/algo/lab6/src")
from game_server import game_server
import unittest


class TestGameServer(unittest.TestCase):
    def test_3_clients(self):
        server = "6 6\n 1 2 6\n 1 3 10\n 3 4 80\n 4 5 50\n 5 6 20\n 2 3 40\n 2 4 100\n"
        expected_result = "100"
        with open("gamsrv.in", "w") as file_in:
            file_in.write(server)
        game_server()
        with open("gamsrv.out", "r") as file_out:
            gamsrv_out = file_out.read().strip()
            self.assertEqual(gamsrv_out, expected_result)

    def test_all_nodes_are_clients(self):
        server = "3 2\n 1 2 3 \n 1 2 5\n 2 3 8\n"
        expected_result = "inf"
        with open("gamsrv.in", "w") as file_in:
            file_in.write(server)
        game_server()
        with open("gamsrv.out", "r") as file_out:
            gamsrv_out = file_out.read().strip()
            self.assertEqual(gamsrv_out, expected_result)

    def test_all_nodes_are_servers(self):
        server = "3 0\n"
        expected_result = "inf"
        with open("gamsrv.in", "w") as file_in:
            file_in.write(server)
        game_server()
        with open("gamsrv.out", "r") as file_out:
            gamsrv_out = file_out.read().strip()
            self.assertEqual(gamsrv_out, expected_result)


if __name__ == "__main__":
    unittest.main()
