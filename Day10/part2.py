file_name = "test_input.txt"


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

    pixels = []
    register_count = 1
    for cycle in range(240):
        register_count = (
            total_cycles_count[cycle]
            if cycle in total_cycles_count
            else total_cycles_count[cycle + 1]
        )
        sprite = (register_count - 1, register_count, register_count + 1)

        index = cycle % 40

        if cycle in total_cycles_count and index in sprite:
            pixels.append("#")
        elif cycle + 1 in total_cycles_count and index in sprite:
            pixels.append("#")
        else:
            pixels.append(".")
    for chunk in chunks(pixels, 40):
        print("".join(chunk))

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


if __name__ == "__main__":
    print(cathode_Ray_tube(file_name))
