file_name = "sample_input.txt"


def file_read(file):
    commands = []
    for line in file:
        commands.append(line.strip().split(" "))
    return commands


def cathode_Ray_tube(file_name):
    with open(file_name, "r") as file:
        commands = file_read(file)

    cycle = register_value = 1
    total_cycles_count = {cycle: register_value}

    for command in commands:
        match command:
            case ["noop"]:
                cycle += 1
            case ["addx", value]:
                cycle += 2
                register_value += int(value)
        total_cycles_count[cycle] = register_value

    signal_strengths_cycles = (20, 60, 100, 140, 180, 220)
    total_sum = 0
    for signal in signal_strengths_cycles:
        if signal in total_cycles_count:
            total_sum += total_cycles_count[signal] * signal
        elif signal - 1 in total_cycles_count:  # in the middle of the second addx -1
            total_sum += total_cycles_count[signal - 1] * signal

    return total_sum


if __name__ == "__main__":
    print(cathode_Ray_tube(file_name))
