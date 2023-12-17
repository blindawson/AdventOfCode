from AdventOfCode.support import support
from itertools import product


class Springs:
    def __init__(self, filename, part2=False):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.part2 = part2

    def calc_arrangements(self):
        sum = 0
        for item in self.file_input:
            item[1] = self.preprocess_group_input(item[1])
            if self.part2:
                item[0] = ((item[0] + "?") * 5)[:-1]
                item[1] = item[1] * 5
            item[0] = self.grouped_row(item[0])
            sum += self.calc_combinations(item[0], item[1])
        return sum

    # Split the input string into groups of # and ?
    def grouped_row(self, row: str):
        return [x for x in row.split(".") if x]

    # Turn group_input from str into list of ints
    def preprocess_group_input(self, group: str):
        return [int(x) for x in group.split(",")]

    # Make a list of all possible combinations for a given string
    def row_combos(self, text: str):
        q_count = text.count("?")
        dot_hash_combinations = list(product([".", "#"], repeat=q_count))
        row_combinations = []

        for dot_hash in dot_hash_combinations:
            row_combination = text
            for i in dot_hash:
                row_combination = row_combination.replace("?", i, 1)
            row_combinations.append(row_combination)
        return row_combinations

    # List the size of each group in a row
    def row_count(self, row: str):
        return [len(x) for x in self.grouped_row(row)]

    def group2txt(self, group: list):
        txt = ""
        for g in group:
            txt += "." + "#" * g + "."
        return txt

    def test_text(self, text: list, groups: list):
        options = []
        for i in [".", "#"]:
            text1 = text.replace("?", i, 1)
            if "?" in text1:
                start_text1_str = text1[: text1.find("?")]
                start_text1_int = self.row_count(start_text1_str)
                if (start_text1_int[:-1] == groups[: len(start_text1_int[:-1])]) and (
                    start_text1_int[-1] <= groups[len(start_text1_int) - 1]
                ):
                    options.append(text1)
            else:
                start_text1_str = text1
                start_text1_int = self.row_count(start_text1_str)
                if start_text1_int == groups:
                    options.append(text1)
            
        return options

    def calc_combinations(
        self, dashdot: list, group_sizes: list, previous_groups: list = []
    ):
        combo_strs = self.row_combos(dashdot[0])
        group_dict = {}
        combo_sum = 0
        for combo_str in combo_strs:
            combo_int = previous_groups + self.row_count(combo_str)
            if combo_int == group_sizes[: len(previous_groups + combo_int)]:
                if tuple(combo_int) in group_dict.keys():
                    group_dict[tuple(combo_int)] += 1
                else:
                    group_dict[tuple(combo_int)] = 1
        if len(dashdot) > 1:
            for key, value in group_dict.items():
                new_dashdot = [self.group2txt(key) + "." + dashdot[1]] + dashdot[2:]
                combo_sum += self.calc_combinations(new_dashdot, group_sizes) * value
        else:
            for key, value in group_dict.items():
                if list(key) == group_sizes:
                    combo_sum += value
        return combo_sum


filename = r"year_2023/tests/test_inputs/12_test_input.txt"
# filename = r"year_2023/input/12_hot_springs.txt"

m = Springs(filename, part2=True)
# m.test_text('.#.###.#.#####?', [1, 3, 1, 6])
m.test_text(".??..??...?##.", [1,1,3])

# No recursive, just loop switching back and forth between ints and strs