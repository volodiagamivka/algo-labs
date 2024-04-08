from collections import deque


class Islands:
    def num_of_islands(self, matrix):
        islands = 0
        rows = len(matrix)
        columns = len(matrix[0])
        visited = set()
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == "1" and (i, j) not in visited:
                    self.bfs(matrix, i, j, visited)
                    islands += 1
        return islands

    def bfs(self, matrix, i, j, visited):
        queue = deque()
        queue.append((i, j))
        visited.add((i, j))
        while queue:
            i, j = queue.pop()
            neighbors = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
                (i + 1, j + 1),
                (i + 1, j - 1),
                (i - 1, j + 1),
                (i - 1, j - 1),
            ]
            for k, l in neighbors:
                if (
                    k in range(len(matrix))
                    and l in range(len(matrix[0]))
                    and (k, l) not in visited
                ):
                    if matrix[k][l] == "1":
                        visited.add((k, l))
                        queue.append((k, l))
