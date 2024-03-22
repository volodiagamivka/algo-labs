class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def heap_sort(self, array, n, i):
        max_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and array[left_child].priority > array[max_index].priority:
            max_index = left_child

        if right_child < n and array[right_child].priority > array[max_index].priority:
            max_index = right_child

        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self.heap_sort(array, n, max_index)

    def insert_to_queue(self, value, priority):
        node = Node(value, priority)
        self.queue.append(node)
        n = len(self.queue)
        for i in range(n // 2, -1, -1):
            self.heap_sort(self.queue,n, i)

    def delete_max_pr_el(self):
        if self.queue:
            el_for_deleting = self.queue[0]
            self.queue[0] = self.queue[-1]
            self.queue.pop()
            self.heap_sort(self.queue, len(self.queue), 0)
            return el_for_deleting

    def display_queue(self):
        for node in self.queue:
            print(f"Значення:{node.value},Пріоритет:{node.priority}")

