import csv


def floyd_warshall(graph):
    
    dist = [[float("inf")] * len(graph) for vertex in range(len(graph))]

    for rows in range(len(graph)):
        for cols in range(len(graph)):
            if graph[rows][cols] != 0:
                dist[rows][cols] = graph[rows][cols]
            elif rows == cols:
                dist[rows][cols] = 0

    for k in range(len(graph)):
        for rows in range(len(graph)):
            for cols in range(len(graph)):
                dist[rows][cols] = min(dist[rows][cols], dist[rows][k] + dist[k][cols])

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
