import unittest
from heap import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_insertion(self):
        pq = PriorityQueue()
        pq.insert_to_queue(1, 3)
        pq.insert_to_queue(2, 7)
        pq.insert_to_queue(3, 5)
        pq.insert_to_queue(4,4)

        expected_queue = [(2,7), (3,5), (4,4), (1,3)]
        actual_queue = [(node.value,node.priority) for node in pq.queue]
        self.assertEqual(actual_queue, expected_queue)

    def test_removing(self):
        pq = PriorityQueue()
        pq.insert_to_queue(1,5)
        pq.insert_to_queue(2,3)
        pq.insert_to_queue(3,8)
        pq.insert_to_queue(4,2)
        pq.delete_max_pr_el()
        expected_queue = [(1,5),(2,3),(4,2)]
        actual_queue = [(node.value,node.priority) for node in pq.queue]
        self.assertEqual(actual_queue, expected_queue)

    def test_display_queue(self):
        pq = PriorityQueue()
        pq.insert_to_queue(1, 5)
        pq.insert_to_queue(2, 3)
        pq.insert_to_queue(3, 8)
        pq.insert_to_queue(4, 2)

        expected_output = [(8, 3), (5, 1), (3, 2), (2, 4)]
        actual_output = [(node.value, node.priority) for node in pq.queue]

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
