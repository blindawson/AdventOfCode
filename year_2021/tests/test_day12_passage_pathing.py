from year_2021.src import day12_passage_pathing as pp

input1 = pp.read_file('year_2021/tests/test_inputs/12_test_input_1.txt')
input2 = pp.read_file('year_2021/tests/test_inputs/12_test_input_2.txt')

def test_add_to_path():
    path_list = pp.add_to_path(path_list=[['start']], path_base=['start'], new_caves=['a', 'b'])
    assert path_list == [['start', 'a'], ['start', 'b']]
    path_list = pp.add_to_path(path_list=path_list, path_base=['start', 'b'], new_caves=['B', 'b'])
    assert path_list == [['start', 'a'], ['start', 'b', 'B']]


def test_find_adjacent():
    adjacent_caves = pp.find_adjacent('A', input1)
    adjacent_caves.sort()
    result = ['start', 'end', 'c', 'b']
    result.sort()
    assert adjacent_caves == result


def test_continue_paths():
    path_list = pp.continue_paths(input1, [['start']])
    assert path_list == [['start', 'A'], ['start', 'b']]
    path_list = pp.continue_paths(input1, path_list)
    assert path_list == [['start', 'A', 'c'], ['start', 'A', 'b'], ['start', 'A', 'end'], 
                         ['start', 'b', 'A'], ['start', 'b', 'd'], ['start', 'b', 'end']]


def test_count_paths():
    assert pp.count_paths(input1) == 10
    assert pp.count_paths(input2) == 19