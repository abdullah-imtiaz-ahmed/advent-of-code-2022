import re
import itertools

file_name = "sample_input.txt"


def read_and_parse_file(file):
    stacks, moves = [], []
    parse_moves = False
    for line in file:
        if line.strip() == "":
            parse_moves = True
            continue

        elif not parse_moves:
            line = list(line)
            crates = []
            for index in range(0, len(line), 4):
                index_slice = slice(index, index + 4)
                line_data = line[index_slice]
                crates.append("".join(line_data).strip())
            stacks.append(crates)

        else:
            move = [int(digit) for digit in re.findall(r"\d+", line)]
            moves.append(move)
    return stacks, moves


def supply_stacks(file_name):
    with open(file_name, "r") as file:
        stacks, moves = read_and_parse_file(file)
        stacks = filter_empty_values(matrix_transpose(stacks[:-1]))
    for move in moves:
        number_of_items, from_, to = move
        from_, to = from_ - 1, to - 1
        value = stacks[from_][:number_of_items]
        stacks[from_] = stacks[from_][number_of_items:]
        stacks[to] = value + stacks[to]

    crate_on_top_of_stack = []
    for stack in stacks:
        crate_on_top_of_stack.append(stack[0][1])
    return "".join(crate_on_top_of_stack)


def matrix_transpose(matrix):
    return [list(item) for item in itertools.zip_longest(*matrix)]


def filter_empty_values(stacks):
    filtered_stack = []
    for stack in stacks:
        filtered_stack.append([value for value in stack if value])
    return filtered_stack


if __name__ == "__main__":
    print(supply_stacks(file_name))
