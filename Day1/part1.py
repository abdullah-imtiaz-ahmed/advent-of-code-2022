file_name = 'sample_input.txt'


def file_read_gen(file):
    calories_count = []
    for line in file:
        line = line.strip()
        if line == '':
            yield calories_count
            calories_count = []
            continue
        calories_count.append(int(line))
    yield calories_count


def compute_max_calory(file_name):
    elf_calory_count = []
    with open(file_name, 'r') as file:
        for calories_count in file_read_gen(file):
            elf_calory_count.append(sum(calories_count))
    return max(elf_calory_count)


if __name__ == "__main__":  
    print(compute_max_calory(file_name))
