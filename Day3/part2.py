import string
from collections import ChainMap

upper_case_alphabets = string.ascii_uppercase

lower_case_alphabets_with_priorities = {
    alphabet: index for index, alphabet in enumerate(string.ascii_lowercase, 1)
}
upper_case_alphabets_with_priorities = {
    alphabet: index for index, alphabet in enumerate(string.ascii_uppercase, 27)
}
lookup_dictionary = ChainMap(
    lower_case_alphabets_with_priorities, upper_case_alphabets_with_priorities
)
file_name = "sample_input.txt"


def file_read_gen(file):
    group = []
    for line in file:
        line = line.strip()
        if line:
            group.append(line)
        if len(group) == 3:
            yield group
            group = []


def common_items_in_compartments(file_name):
    common_items = []
    with open(file_name, "r") as file:
        for item in file_read_gen(file):
            intersection = get_intersection_of_strings(item).pop()
            common_items.append(lookup_dictionary[intersection])
    return sum(common_items)


def get_intersection_of_strings(list_of_strings):
    result = set(list_of_strings[0])
    for string_ in list_of_strings[1:]:
        result.intersection_update(string_)
    return result


if __name__ == "__main__":
    print(common_items_in_compartments(file_name))
