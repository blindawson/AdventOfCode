from AdventOfCode.year_2022.src import day23_unstable_diffusion as d23


def test_example():
    filename = r"year_2022/tests/test_inputs/23_test_input.txt"
    m = d23.ElfMap(filename)
    assert m.part1_answer == 110


def test_part1():
    filename = r"year_2022/input/23_unstable_diffusion.txt"
    m = d23.ElfMap(filename)
    assert m.part1_answer == 3947


def test_example_part2():
    filename = r"year_2022/tests/test_inputs/23_test_input.txt"
    m = d23.ElfMap(filename, part2=True)
    assert m.round == 20


def test_part2():
    filename = r"year_2022/input/23_unstable_diffusion.txt"
    m = d23.ElfMap(filename, part2=True)
    assert m.round == 1012
