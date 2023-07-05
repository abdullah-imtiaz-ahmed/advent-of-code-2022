import string
from collections import ChainMap
upper_case_alphabets = string.ascii_uppercase

lower_case_alphabets_with_priorities = {alphabet: index for index, alphabet in enumerate(string.ascii_lowercase, 1)}
upper_case_alphabets_with_priorities = {alphabet: index for index, alphabet in enumerate(string.ascii_uppercase, 27)}
lookup_dictionary = ChainMap(lower_case_alphabets_with_priorities, upper_case_alphabets_with_priorities)
file_name = "sample_input.txt"


def file_read_gen(file):
    for line in file:
        yield line.strip()


def common_items_in_compartments(file_name):
    common_items = []
    with open(file_name, 'r') as file:
        for item in file_read_gen(file):
            first_half = set(item[:len(item) // 2])
            second_half = set(item[len(item) // 2:])
            common_item = first_half.intersection(second_half).pop()
            common_items.append(lookup_dictionary[common_item])
    return sum(common_items)


if __name__ == "__main__":  
    print(common_items_in_compartments(file_name))