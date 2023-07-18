# This program might not be work for all inputs.
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
righ_left_up_down = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)
diagonal_positions = (
    (1, -1),
    (1, 1),
    (-1, 1),
    (-1, -1),
)


def rope_bridge(file_name):
    with open(file_name, "r") as file:
        moves = file_read(file)
        range_ = 9
    knots = list(range(range_, -1, -1))
    positions = [start_position for _ in range(len(knots))]
    previous_positions = positions.copy()
    tail_position_count = set()
    tail_position_count.add(start_position)

    for move in moves:
        _, count = move
        for _ in range(count):
            for index, position in enumerate(positions):
                # compute head
                if index == 0:
                    previous_positions[0] = positions[0]
                    positions[0] = compute_head_position(position, move)
                    continue

                # save previous position
                previous_positions[index] = positions[index]
                current_head_position = positions[index - 1]
                previous_head_position = previous_positions[index - 1]
                current_tail = positions[index]
                tail_position = compute_tail_position(
                    current_head_position, previous_head_position, current_tail, move
                )

                positions[index] = tail_position
                if index == len(positions) - 1:
                    tail_position_count.add(positions[index])
    return len(tail_position_count)


def compute_tail_position(
    current_head_position, previous_head_position, tail_position, move
):
    adjacent_positions_with_difference_one = righ_left_up_down + diagonal_positions

    head_row, head_column = current_head_position
    tail_row, tail_column = tail_position
    position_difference = ((head_row - tail_row), (head_column - tail_column))

    # return same tail position
    if (
        position_difference == start_position
        or position_difference in adjacent_positions_with_difference_one
    ):
        return tail_position

    direction, _ = move
    if (direction in row_directions and head_column == tail_column) or (
        direction in column_directions and head_row == tail_row
    ):
        # return previous_head_position
        for position in righ_left_up_down:
            tail_row, tail_column = tail_position
            row, column = position
            new_position = (tail_row + row, tail_column + column)
            if new_position == previous_head_position:
                return previous_head_position

    for position in diagonal_positions:
        tail_row, tail_column = tail_position
        row, column = position
        new_tail_position = (tail_row + row, tail_column + column)
        new_row, new_column = new_tail_position
        current_row, current_column = current_head_position
        position_difference = ((new_row - current_row), (new_column - current_column))
        if position_difference in adjacent_positions_with_difference_one:
            return new_tail_position


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
