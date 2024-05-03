import csv


def floyd_warshall(graph):
    N = len(graph)
    dist = [[float("inf")] * N for vertex in range(N)]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
            elif i == j:
                dist[i][j] = 0

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def open_file(input):
    graph = []
    with open(input, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            graph.append(list(map(int, row)))
    return graph


def min_length_of_cable(graph):
    shortest_ways = floyd_warshall(graph)
    total_length = 0
    for row in shortest_ways:
        total_length += sum(row)

    return total_length
