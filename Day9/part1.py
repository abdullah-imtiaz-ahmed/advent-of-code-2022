file_name = "sample_input.txt"


def file_read(file):
    moves = []  # (direction, count)
    for line in file:
        direction, count = line.strip().split(" ")
        moves.append((direction, int(count)))
    return moves


right, left, up, down = "R", "L", "U", "D"
row_directions, column_directions = (right, left), (up, down)  # (direction, direction)
start_position = (0, 0)


def rope_bridge(file_name):
    with open(file_name, "r") as file:
        moves = file_read(file)
    head_position, last_visited_head_position, tail_position = (
        start_position,
        start_position,
        start_position,
    )
    tail_positions_count = set()
    tail_positions_count.add(start_position)

    for move in moves:
        _, count = move
        for _ in range(count):
            head_position = compute_head_position(head_position, move)
            tail_position = compute_tail_position(
                head_position, last_visited_head_position, tail_position
            )
            last_visited_head_position = head_position
            tail_positions_count.add(tail_position)

    return len(tail_positions_count)


def compute_tail_position(head_position, last_visited_head_position, tail_position):
    adjacent_positions_with_difference_one = (
        (0, 0),  # (0,0) is the same position
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, -1),
        (1, 1),
        (-1, 1),
        (-1, -1),
    )
    head_row, head_column = head_position
    tail_row, tail_column = tail_position
    position_difference = ((head_row - tail_row), (head_column - tail_column))

    if position_difference in adjacent_positions_with_difference_one:
        return tail_position

    return last_visited_head_position


def compute_head_position(current_position, move):
    direction, _ = move
    row, column = current_position

    if direction in row_directions:
        if direction == right:
            new_position = (row + 1, column)
        else:
            # direction == left
            new_position = (row - 1, column)
    else:
        # direction in column_directions
        if direction == down:
            new_position = (row, column + 1)
        else:
            # direction == up
            new_position = (row, column - 1)
    return new_position


if __name__ == "__main__":
    print(rope_bridge(file_name))
