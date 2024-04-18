from collections import deque


def dijkstra(graph, start_point):
    dist_to = {}
    for vertex in range(len(graph)):
        dist_to[vertex] = float("inf")

    dist_to[start_point] = 0

    queue = deque()
    queue.append((start_point, 0))

    while queue:
        current_vertex, current_distance = queue.pop()
        if current_distance > dist_to[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            if current_distance + weight < dist_to[neighbor]:
                dist_to[neighbor] = current_distance + weight
                queue.append((neighbor, current_distance + weight))

    return dist_to


def game_server():
    with open("gamsrv.in", "r") as input_file:
        N, M = map(int, input_file.readline().split())
        clients = set(map(int, input_file.readline().strip().split()))
        graph = [[] for i in range(N)]

        for j in range(M):
            startnode, endnode, latency = map(int, input_file.readline().split())
            graph[startnode - 1].append([endnode - 1, latency])
            graph[endnode - 1].append([startnode - 1, latency])

    min_max_latency = float("inf")

    for server_node in range(1, N + 1):
        if server_node not in clients:
            max_latency = max(dijkstra(graph, server_node - 1).values())
            if max_latency < min_max_latency:
                min_max_latency = max_latency

    with open("gamsrv.out", "w") as output_file:
        output_file.write(str(min_max_latency))

    return min_max_latency
