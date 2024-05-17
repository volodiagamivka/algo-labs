def number_of_routes():
    with open("ijones.in", "r") as input_data:
        width, height = map(int, input_data.readline().strip().split())
        matrix = [input_data.readline().strip() for _ in range(height)]

    num_of_ways = [
        [0] * width for i in range(height)
    ]  # create a matrix, each element in the matrix is set to 0

    for row in range(height):
        num_of_ways[row][0] = 1

    for col in range(1, width):
        for row in range(height):
            # Direct move from the left

            num_of_ways[row][col] += num_of_ways[row][col - 1]

            # Check possible jumps from previous columns with the same symbol
            for i in range(height):
                if matrix[row][col] == matrix[i][col - 2]:
                    num_of_ways[row][col] += num_of_ways[i][col - 2]
            # Check possible diagonal jumps upwards
            if row > 0 and matrix[row][col] == matrix[row - 1][col - 1]:
                num_of_ways[row][col] += num_of_ways[row - 1][col - 1]

            # Check possible diagonal jumps downwards
            if row < height - 1 and matrix[row][col] == matrix[row + 1][col - 1]:
                num_of_ways[row][col] += num_of_ways[row + 1][col - 1]

    # return a result from the first and last rows of the last columns
    result = num_of_ways[0][width - 1] + num_of_ways[height - 1][width - 1]

    with open("ijones.out", "w") as output_data:
        output_data.write(str(result))
