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
            # item[0] = self.grouped_row(item[0])
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
        return [row[-1]] + [len(x) for x in self.grouped_row(row)]

    def group2txt(self, group: list):
        txt = ""
        for g in group[1:]:
            txt += "." + "#" * g
        if group[0] == ".":
            txt += "."
        return txt

    def test_text(self, text: str, groups: list, bonus: int):
        options = []
        if text[-1] == "?":
            for i in [".", "#"]:
                new_text = text.replace("?", i)
                text_int = self.row_count(new_text)
                if self.compare_groups(text_int, groups, bonus):
                    options.append(new_text)
        else:
            options.append(text)
        return options

    def compare_groups(self, groups1: list, groups2: list, bonus: int):
        groups1 = groups1[1:]
        if len(groups1) == 0:
            return True
        solid = groups1[:-1]
        if not solid == groups2[: len(solid)]:
            return False
        end_max = groups1[-1] + bonus
        if (
            (len(groups1) <= len(groups2))
            and (groups2[len(solid)] >= groups1[-1])
            and (groups2[len(solid)] <= end_max)
        ):
            return True
        else:
            return False

    def calc_combinations(self, text: str, groups: list):
        group_dict = {("."): 1}
        for i in range(len(text)):
            next_char = text[i]
            remaining_str = text[i + 1 :]
            new_dict = {}
            for key, value in group_dict.items():
                new_text = self.group2txt(key) + next_char
                if "." in remaining_str:
                    bonus = remaining_str.find(".")
                else:
                    bonus = len(remaining_str)
                text_list = m.test_text(new_text, groups, bonus)
                for t in text_list:
                    grouped = tuple(self.row_count(t))
                    if grouped in new_dict.keys():
                        new_dict[grouped] += value
                    else:
                        new_dict[grouped] = value
            group_dict = new_dict
        new_dict = {}
        for key, value in group_dict.items():
            if key[1:] in new_dict.keys():
                new_dict[key[1:]] += value
            else:
                new_dict[key[1:]] = value
        group_dict = new_dict
        return group_dict[tuple(groups)]
