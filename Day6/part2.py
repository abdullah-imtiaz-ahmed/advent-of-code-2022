file_name = "test_input.txt"


def tuning_trouble(file_name):
    with open(file_name, "r") as f:
        data = f.read().replace("\n", "")

    marker = 14
    for index in range(0, len(data) - marker):
        if len(set(data[index:index + marker])) == marker:
            return index + marker
    return 0


if __name__ == "__main__":
    print(tuning_trouble(file_name))
