from typing import List, Tuple, Set


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, x: int, y: int) -> None:
        if x not in self.graph:
            self.graph[x] = set()
        if y not in self.graph:
            self.graph[y] = set()
        self.graph[x].add(y)

    def is_valid_order(self, order: List[int]) -> bool:
        order_set = set(order)
        pos = {val: idx for idx, val in enumerate(order)}

        for vertex in self.graph:
            if vertex in order_set:
                for neighbour in self.graph[vertex]:
                    if neighbour in order_set:
                        if pos[vertex] > pos[neighbour]:
                            return False
        return True

    def must_come_before(self, a: int, b: int, nodes: Set[int]) -> bool:
        if a not in self.graph:
            return False

        # Exact match rule
        if b in self.graph[a]:
            return True

        # Dependent rules
        for other_node in nodes:
            if other_node in self.graph[a] and b in self.graph[other_node]:
                return True
        return False

    def is_valid_position(self, item: int, array_position: int, item_list: List[int], all_nodes: Set[int]) -> bool:

        left_side_list = item_list[:array_position]
        right_side_list = item_list[array_position:]
        test_list = left_side_list + [item] + right_side_list

        for i in range(len(test_list)):
            a = test_list[i]
            for j in range(i + 1, len(test_list)):
                b = test_list[j]
                if self.must_come_before(b, a, all_nodes):
                    return False
        return True

    def get_insertion_position(self, item: int, sorted_list: List[int], nodes: Set[int]) -> int:
        for position in range(len(sorted_list) + 1):
            if self.is_valid_position(item, position, sorted_list, nodes):
                return position
        return -1

    def sort_subset(self, nodes: Set[int]) -> List[int]:
        sorted_list = []
        elements = list(nodes)
        sorted_list.append(elements[0])
        for item in elements[1:]:
            position = self.get_insertion_position(item, sorted_list, nodes)
            if position != -1:
                sorted_list.insert(position, item)
            else:
                sorted_list.append(item)
        return sorted_list


def read_rules_file(filename: str) -> List[Tuple[int, int]]:
    rules = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split('|'))
                rules.append((x, y))
    return rules


def read_updates_file(filename: str) -> List[List[int]]:
    updates = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                update = list(map(int, line.split(',')))
                updates.append(update)
    return updates


def find_middle_number(sequence: List[int]) -> int:
    return sequence[len(sequence) // 2]


graph = Graph()
rules = read_rules_file('resources/safety-page-rules.txt')
updates = read_updates_file('resources/safety-page-updates.txt')

for x, y in rules:
    graph.add_edge(x, y)

valid_middle_numbers = []
invalid_sorted_middle_numbers = []

for i, update in enumerate(updates, 1):
    if graph.is_valid_order(update):
        middle = find_middle_number(update)
        valid_middle_numbers.append(middle)
        print(f"Update {i} is valid. Middle number: {middle}")
    else:
        sorted_sequence = graph.sort_subset(set(update))
        middle = find_middle_number(sorted_sequence)
        invalid_sorted_middle_numbers.append(middle)
        print(f"Update {i} is invalid. After sorting: {sorted_sequence}. New middle: {middle}")

result = sum(valid_middle_numbers)
sorted_sum = sum(invalid_sorted_middle_numbers)

print(f"\nSum of valid middle numbers: {result}")
print(f"Sum of sorted invalid updates: {sorted_sum}")
