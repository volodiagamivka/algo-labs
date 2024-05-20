def number_of_routes():
    with open("ijones.in", "r") as input_data:
        width, height = map(int, input_data.readline().strip().split())
        matrix = [input_data.readline().strip() for _ in range(height)]

    num_of_ways = [[0] * width for _ in range(height)]

    for row in range(height):
        num_of_ways[row][0] = 1

    for col in range(1, width):
        paths = {}
        for row in range(height):
            if matrix[row][col] not in paths:
                paths[matrix[row][col]] = 0
            paths[matrix[row][col]] += num_of_ways[row][col - 1]
        for row in range(height):
            num_of_ways[row][col] += paths[matrix[row][col]]

    result = sum(num_of_ways[row][width - 1] for row in range(height))

    with open("ijones.out", "w") as output_data:
        output_data.write(str(result))
