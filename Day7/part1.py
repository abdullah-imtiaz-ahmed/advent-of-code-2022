from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


file_name = "test_input.txt"


@dataclass
class Node:
    name: str
    size: int = 0
    is_directory: bool = False
    parent: Optional[Node] = None
    children: list = field(default_factory=list)


class Tree:
    def __init__(self):
        self._root = Node(is_directory=True, name="/")
        self.current = self._root

    def add_child(self, child):
        self.current.children.append(child)

    def go_to_root(self):
        self.current = self._root

    def go_to_parent(self):
        self.current = self.current.parent

    def filter_child(self, name):
        self.current = [child for child in self.current.children if child.name == name][0]


def file_read_gen(file):
    for line in file:
        yield line.strip()


def print_children(node, level):
    if node.is_directory:
        print(f"{'--' * level} {node.name} (directory) ({get_size(node)})")
    else:
        print(f"{'--' * level} {node.name} (file) ({get_size(node)})")
    if len(node.children):
        for child in node.children:
            print_children(child, level + 1)


def get_size(node):
    if node.is_directory:
        count = 0
        for child in node.children:
            count += get_size(child) if child.is_directory else child.size
        return count
    else:
        return node.size


at_most_directory_size = 100000


def find_subdirectories(node):
    dir_sizes = 0
    if node.is_directory:
        for child in node.children:
            size = get_size(child)
            if child.is_directory and size <= at_most_directory_size:
                dir_sizes += size + find_subdirectories(child)
            else:
                dir_sizes += find_subdirectories(child)
    return dir_sizes


def no_space_left_on_device(file_name):
    tree = Tree()
    with open(file_name, "r") as file:
        file_read_generator = file_read_gen(file)
        for line in file_read_generator:
            # end of file
            if not line:
                break

            if line.endswith("ls"):
                for line in file_read_generator:
                    if line.startswith("$"):
                        break

                    if line.startswith("dir"):
                        _, name = line.split(" ")
                        node = Node(is_directory=True, name=name, parent=tree.current)
                    else:
                        size, name = line.split(" ")
                        node = Node(name=name, size=int(size), parent=tree.current)
                    tree.add_child(node)

            # goto root
            if line.endswith("/"):
                tree.go_to_root()
            # go up one step
            elif line.endswith(".."):
                tree.go_to_parent()

            elif "cd" in line:
                # find child node
                _, _, name = line.split(" ")
                tree.filter_child(name)

    # print_children(tree._root, 0)
    # print(get_size(tree._root))
    return find_subdirectories(tree._root)


if __name__ == "__main__":
    print(no_space_left_on_device(file_name))
