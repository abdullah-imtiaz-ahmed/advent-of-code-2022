file_name = "test_input.txt"


def tuning_trouble(file_name):
    with open(file_name, "r") as f:
        data = f.read().replace("\n", "")

    for index in range(0, len(data) - 4):
        if len(set(data[index:index + 4])) == 4:
            return index + 4
    return 0


if __name__ == "__main__":
    print(tuning_trouble(file_name))
