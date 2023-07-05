file_name = "sample_input.txt"


def file_read_gen(file):
    for line in file:
        line = line.strip().split(",")
        yield line


def camp_cleanup(file_name):
    pairs_that_overlap = 0
    with open(file_name, "r") as file:
        for item in file_read_gen(file):
            first, second = item
            first, second = generate_sections(first), generate_sections(second)
            if first.issubset(second) or second.issubset(first):
                pairs_that_overlap += 1

    return pairs_that_overlap


def generate_sections(range_):
    start, end = [int(value) for value in range_.split("-")]
    return set(range(start, end + 1))


if __name__ == "__main__":
    print(camp_cleanup(file_name))
