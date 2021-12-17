from copy import deepcopy

def read_file(filename):
    connections_file = open(filename).read().splitlines()
    connections = [x.split('-') for x in connections_file]
    return connections


def add_to_path(path_list, path_base, new_caves):
    current_path = deepcopy(path_base)
    added_new_path = False
    for new_cave in new_caves:
        if new_cave.isupper():
            path_list.append(current_path + [new_cave])
            added_new_path = True
        elif new_cave == 'start':
            continue
        elif new_cave.islower():
            if new_cave not in current_path:
                path_list.append(current_path + [new_cave])
                added_new_path = True
            elif 'double cave' not in current_path:
                path_list.append(['double cave'] + current_path + [new_cave])
                added_new_path = True
    if not added_new_path:
        path_list.append(current_path + ['quit'])
    path_list.remove(current_path)
    return path_list


def find_adjacent(current_cave, connections_list):
    adjacent_caves = []
    for connection in connections_list:
        if current_cave in connection:
            adjacent_cave = (set(connection) - {current_cave}).pop()
            adjacent_caves.append(adjacent_cave)
    return adjacent_caves


def continue_paths(connections_list, path_list_initial):
    path_list = deepcopy(path_list_initial)
    for path in path_list_initial:
        if (path[-1] != 'end') & (path[-1] != 'quit'): 
            adjacent_caves = find_adjacent(path[-1], connections_list)
            path_list = add_to_path(path_list, path, adjacent_caves)
    return path_list


def count_paths(connections, paths=None):
    if not paths:
        paths = [['start']]
    end_caves = [path[-1] for path in paths]
    remove_quit_end = set(end_caves) - {'end'} - {'quit'}
    while len(remove_quit_end) > 0:
        paths = continue_paths(connections, paths)
        end_caves = [path[-1] for path in paths]
        remove_quit_end = set(end_caves) - {'end'} - {'quit'}
    end_caves = [path[-1] for path in paths]
    return sum(1 for x in end_caves if x == 'end')


connections = read_file(r'year_2021/input/12_passage_pathing.txt')
test_input1 = read_file(r'year_2021/tests/test_inputs/12_test_input_1.txt')
print(f'Test 1 answer: {count_paths(test_input1)}')
print(f'Part 1 answer: {count_paths(connections)}')