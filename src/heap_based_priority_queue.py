class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __heapify_down(self, array, n, i):
        
        max_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and array[left_child].priority > array[max_index].priority:
            max_index = left_child

        if right_child < n and array[right_child].priority > array[max_index].priority:
            max_index = right_child

        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self.__heapify_down(array, n, max_index)

    def __heapify_up(self, array, i):
        
        parent = (i - 1) // 2
        if i > 0 and array[i].priority > array[parent].priority:
            array[i], array[parent] = array[parent], array[i]
            self.__heapify_up(array, parent)

    def insert_to_queue(self, value, priority):
        
        node = Node(value, priority)
        self.queue.append(node)
        self.__heapify_up(self.queue, len(self.queue) - 1)

    def delete_max_pr_el(self):
        
        if not self.queue:
            return None
        max_node = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.__heapify_down(self.queue, len(self.queue), 0)
        return max_node

    def display_queue(self):
        
        for node in self.queue:
            print(f"Значення: {node.value}, Пріоритет: {node.priority}")



