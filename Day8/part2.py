import functools
import operator

file_name = "test_input.txt"


def file_read_gen(file):
    for line in file:
        line = line.strip()
        yield [int(i) for i in line]


grid, inner_grid, empty_grid = [], [], []
row_length = column_length = 0
inner_grid_slice = slice(1, -1)


def treetop_tree_house(file_name):
    global row_length, column_length, inner_grid, empty_grid
    with open(file_name, "r") as file:
        for line in file_read_gen(file):
            grid.append(line)

    row_length, column_length = len(grid), len(grid[0])
    inner_grid = [row[inner_grid_slice] for row in grid][inner_grid_slice]
    empty_grid = [[0 for _ in range(row_length)] for _ in range(column_length)]

    for row_index, row_value in enumerate(inner_grid, 1):
        for column_index, column_value in enumerate(row_value, 1):
            empty_grid[row_index][column_index] = find_long_trees(
                row_index, column_index, column_value
            )

    return max([column for row in empty_grid for column in row])


def find_long_trees(row_index, column_index, value):
    right = left = down = up = 0

    # right
    for index in range(column_index + 1, column_length):
        grid_value = grid[row_index][index]
        right += 1
        if grid_value >= value:
            break

    # left
    for index in range(column_index - 1, -1, -1):
        grid_value = grid[row_index][index]
        left += 1
        if grid_value >= value:
            break

    # down
    for index in range(row_index + 1, row_length):
        grid_value = grid[index][column_index]
        down += 1
        if grid_value >= value:
            break

    # up
    for index in range(row_index - 1, -1, -1):
        grid_value = grid[index][column_index]
        up += 1
        if grid_value >= value:
            break

    return functools.reduce(operator.mul, [right, left, up, down], 1)


if __name__ == "__main__":
    print(treetop_tree_house(file_name))
